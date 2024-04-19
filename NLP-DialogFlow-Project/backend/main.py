from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()
inprogress_orders = {}

@app.post("/")
async def handle_request(request: Request):

    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'order.add - context: ongoing-order': add_to_order,
        'order.remove - context: ongoing-order': remove_from_order,
        'order.complete - context: ongoing-order': complete_order,
        'track.order - context: ongoing-tracking': track_order
    }
    
    return intent_handler_dict[intent](parameters,session_id)

def track_order(parameters : dict):
    print("REcieved context :2")
    order_id = parameters['order_id']
    status = db_helper.get_order_status(order_id)

    if status:
        fullfillmet_text = f"The order status for order id : {order_id} is {status}"
    else :
        fullfillmet_text = f"No order found with order id {order_id}"

    return JSONResponse(content={"fulfillmentText": fullfillmet_text})

def add_to_order(parameters : dict,session_id : str):
    food_items = parameters["food-item"]
    quantities = parameters["number"]

    if len(food_items) != len(quantities):
        fulfillment_text = "Sorry I didn't understand. Can you please specify food items and quantities clearly?"
    else:
        new_food_dict = dict(zip(food_items, quantities))

        if session_id in inprogress_orders:
            current_food_dict = inprogress_orders[session_id]
            current_food_dict.update(new_food_dict)
            inprogress_orders[session_id] = current_food_dict
        else:
            inprogress_orders[session_id] = new_food_dict

        order_str = generic_helper.get_str_from_food_dict(inprogress_orders[session_id])
        fulfillment_text = f"So far you have: {order_str}. Do you need anything else?"

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def remove_from_order(parameters : dict):
    fulfillment_text = "Sorry I didn't understand. Can you please specify food items and quantities clearly?"
    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def complete_order(parameters : dict):
    fulfillment_text = "Sorry I didn't understand. Can you please specify food items and quantities clearly?"
    return JSONResponse(content={"fulfillmentText": fulfillment_text})