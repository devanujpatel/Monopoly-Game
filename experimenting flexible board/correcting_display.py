class token:
    def __init__(token_self,token, token_str , player_str):
        master_dictionary["tokens"][token_str] = {"position":0, "row":row_coordinates["go_box"],"column":column_coordinates["go_box"]}
        master_dictionary["players"][player_str] = {"token_id":token,"token_str":token_str, "money":1500}
        token.grid(row=10,column=10)
