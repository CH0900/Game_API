from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from games import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("reviews", import_name = "reviews")


@blueprint.route('', methods=["POST"])
def new_game():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.NewGame, x, config=config)
    #2. 驗證資料
    #2.1. title不可空白
    if obj.title.strip() == '':
        return json.jsonify(errors.e1001)
    #2.2. genre必須是動作、RPG、解迷這3類
    if obj.genre.strip() not in ['動作','RPG','解迷']:
        return json.jsonify(errors.e1002)

    #3. 建立game
    #3.1. 建立game
    s = datahelper.new_game(obj.title.strip() ,\
                            obj.description.strip() ,\
                            obj.release_date,\
                            obj.genre.strip())
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳review
    return json.jsonify(make_data_result(s))

@blueprint.route('/<game_id>', methods=["GET"])
def get_game(game_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e2001)
    
    
    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e2001) 
    #3. 取得資料
    r = datahelper.get_game(game_id)
    #4. 回傳資料
    return json.jsonify(make_data_result(r))

@blueprint.route('', methods=["GET"])
def get_games():
    #1. 解析JSON或參數
    #2. 驗證資料
    #3. 取得games
    r = datahelper.get_games()
    #4. 回傳games
    return json.jsonify(make_data_result(r))

@blueprint.route('/<game_id>', methods=["UPDATE"])
def update_game(game_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e3001)
    # 1.2. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateGame, x, config=config)

    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e3001) 
    #2.1. title不可空白
    if obj.title.strip() == '':
        return json.jsonify(errors.e3002)
    #2.2. genre必須是動作、RPG、解迷這3類
    if obj.genre.strip() not in ['動作','RPG','解迷']:
        return json.jsonify(errors.e3003)
    
    #3. 更新game
    #3.1. 更新game
    s = datahelper.update_game(game_id ,\
                            obj.title.strip() ,\
                            obj.description.strip() ,\
                            obj.release_date,\
                            obj.genre.strip())
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳review
    return json.jsonify(make_data_result(s))

@blueprint.route('/<game_id>', methods=["DELETE"])
def delete_game(game_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e4001)
    
    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e4001) 
    #3. 取得資料
    #3.1. 刪除game
    r1 = datahelper.delete_game(game_id)
    #3.2. 刪除關聯的player
    r2 = datahelper.delete_game_players(game_id)
    #3.3. 提交
    g.cursor().connection.commit()

    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"sucess:":r1 or r2}))

@blueprint.route('/<game_id>/players', methods=["GET"])
def get_game_players(game_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e5001)
    
    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e5001) 
    #3. 取得資料
    r = datahelper.get_game_players(game_id)
    #4. 回傳資料
    return json.jsonify(make_data_result(r))

@blueprint.route('/<game_id>', methods=["POST"])
def new_game_player(game_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e6001)
    # 1.2. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.NewGamePlayer, x, config=config)
    
    
    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e6001) 
    #2.1. 驗證player_id是否存在
    if  datahelper.is_player_id_existed(obj.player_id) == False:
        return json.jsonify(errors.e6002) 
    #3. 新增資料
    r = datahelper.new_game_player(game_id, obj.player_id)
    #4. 回傳資料
    return json.jsonify(make_data_result(r))

@blueprint.route('/<game_id>/players/<player_id>', methods=["DELETE"])
def delete_game_player(game_id,player_id):
    # 1. 解析JSON或參數
    # 1.1. 解析game_id為int
    try:
        game_id = int(game_id)
    except:
        return json.jsonify(errors.e7001)
    # 1.2. 解析player_id為int
    try:
        player_id = int(player_id)
    except:
        return json.jsonify(errors.e7002)
    
    #2. 驗證資料
    #2.1. 驗證game_id是否存在
    if  isinstance(game_id, int) == False or \
          datahelper.is_game_id_existed(game_id) == False:
        return json.jsonify(errors.e7001) 
    #2.1. 驗證player_id是否存在
    if  isinstance(player_id, int) == False or \
          datahelper.is_player_id_existed(player_id) == False:
        return json.jsonify(errors.e7002) 
    #3. 取得資料
    #3.1. 刪除game_player
    r = datahelper.delete_game_player(game_id,player_id)
    #3.2. 提交
    g.cursor().connection.commit()

    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":r}))

