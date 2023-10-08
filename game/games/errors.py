from results import make_error_result


#給new_game API使用的error
e1001 = make_error_result("e1001","title不可空白")
e1002 = make_error_result("e1002","genre必須是動作、RPG、解迷這3類")

#給get_game API使用的error
e2001 = make_error_result("e2001","game_id不存在")


#給update_game API使用的error
e3001 = make_error_result("e3001","game_id不存在")
e3001 = make_error_result("e3002","title不可空白")
e3002 = make_error_result("e3003","genre必須是動作、RPG、解迷這3類")

#給get_game API使用的error
e4001 = make_error_result("e4001","game_id不存在")

#給get_game_players API使用的error
e5001 = make_error_result("e5001","game_id不存在")

#給new_game_player API使用的error
e6001 = make_error_result("e6001","game_id不存在")
e6002 = make_error_result("e6002","player_id不存在")

#給delete_game_player API使用的error
e7001 = make_error_result("e7001","game_id不存在")
e7002 = make_error_result("e7002","player_id不存在")
