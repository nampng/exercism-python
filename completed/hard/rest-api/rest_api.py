import json

class RestAPI:

    def __init__(self, database=None):
        if database is None:
            self.database = {"users" : []}
        else:
            self.database = database

    def get(self, url, payload=None):
        if payload:
            payload = json.loads(payload)

        print(f"GET: {payload = }")

        if url == '/users':
            if payload:
                name = payload["users"][0]
                print(f"Finding {name}")
                for user in self.database["users"]:
                    if user["name"] == name:
                        response = {"users": [user]}
                        print(f"USERS: {response = }")
                        return json.dumps(response)
                    
                raise Exception("User not found.")

            else:
                return json.dumps(self.database)


    def post(self, url, payload=None):
        if payload:
            payload = json.loads(payload)

        print(f"POST: {payload = }")
        if url == '/add':
            if payload:
                user = {
                    "name": payload["user"],
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
                print(user)
                self.database["users"].append(user)
                return json.dumps(user)
        elif url == '/iou':
            if payload:
                lender = payload["lender"]
                borrower = payload["borrower"]
                lender_entry = None
                borrower_entry = None
                # Go through each user
                for user in self.database["users"]:
                    # If the lender is found
                    if user["name"] == lender:
                        amount = payload["amount"]
                        print("Found lender")
                        print(f"Starting amount: {amount}")

                        # Check if the lender owes the borrower,
                        # strip the owed amount off the current amount
                        if borrower in user["owes"]:
                            if user["owes"][borrower] >= amount:
                                borrowed = user["owes"][borrower]
                                user["balance"] += amount
                                user["owes"][borrower] -= amount
                                amount -= borrowed

                                if user["owes"][borrower] == 0:
                                    user["owes"].pop(borrower)
                            else:
                                borrowed = user["owes"].pop(borrower)
                                user["balance"] += borrowed
                                amount -= borrowed

                        print(f"Remaining amount: {amount}")
                                
                        # Process owed_by
                        if amount > 0:
                            if borrower in user["owed_by"]:
                                user["owed_by"][borrower] += amount
                                user["balance"] += amount
                            else:
                                user["owed_by"][borrower] = amount
                                user["balance"] += amount

                        lender_entry = user

                    # If the borrower is found
                    elif user["name"] == borrower:
                        amount = payload["amount"]
                        print("Found borrower")
                        print(f"Starting amount: {amount}")

                        # Check if the borrower is owed by the lender,
                        # strip the owed by amount by the current amount
                        if lender in user["owed_by"]:
                            if user["owed_by"][lender] >= amount:
                                lent = user["owed_by"][lender]
                                user["balance"] -= amount
                                user["owed_by"][lender] -= amount
                                amount -= lent

                                if user["owed_by"][lender] == 0:
                                    user["owed_by"].pop(lender)
                            else:
                                lent = user["owed_by"].pop(lender)
                                user["balance"] -= lent
                                amount -= lent

                        print(f"Remaining amount: {amount}")

                        # Process owes
                        if amount > 0:
                            if lender in user["owes"]:
                                user["owes"][lender] += amount
                                user["balance"] -= amount
                            else:
                                user["owes"][lender] = amount
                                user["balance"] -= amount

                        borrower_entry = user

                sorted_names = [lender_entry, borrower_entry]
                sorted_names.sort(key=lambda x: x["name"])

                print(f"IOU: {self.database = }")
                print(f"LENDER: {lender_entry}")
                print(f"BORROWER: {borrower_entry}")
                response = {"users": [
                    sorted_names[0],
                    sorted_names[1]
                ]}
                return json.dumps(response)
            


