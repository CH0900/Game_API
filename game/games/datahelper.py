from flask import g

# def add_customer(c):
#     db.append(c)

# def create_product(name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         insert into product
#         (name, price)
#         values
#         (%s, %s)  
#         ''',
#         (name, price)
#     )
#     new_id = cur.lastrowid
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (new_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def get_products():
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product
#         '''
#     )
#     ret_dicts = cur.fetchall()

#     return ret_dicts



# def is_product_id_existed(product_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product where product_id=%s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict != None

# def get_product(product_id):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         select * from product where product_id=%s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict

# def update_product(product_id, name, price):
#     cur = g.cursor()
#     cur.execute(
#         '''
#         update product
#         set name=%s, price=%s
#         where product_id=%s 
#         ''',
#         (name, price, product_id)
#     )
#     cur.execute(
#         '''
#         select * from product where product_id = %s
#         ''',
#         (product_id)
#     )
#     ret_dict = cur.fetchone()

#     return ret_dict


# def delete_product(product_id):
    # cur = g.cursor()
    # cur.execute(
    #         '''
    #         delete from product where product_id=%s
    #         ''',
    #         (product_id)
    #     )
 
    # rowcount = cur.rowcount
    
    # return rowcount > 0


def new_game(title ,\
            description,\
            release_date,\
            genre):
    cur = g.cursor()
    cur.execute(
        '''
        insert into game
        (title ,description,release_date,genre)
        values
        (%s, %s, %s, %s)  
        ''',
        (title ,description,release_date,genre)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from game where game_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def is_game_id_existed(game_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from game where game_id=%s
        ''',
        (game_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

def get_game(game_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from game where game_id=%s
        ''',
        (game_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def get_games():
    cur = g.cursor()
    cur.execute(
        '''
        select * from game
        ''',
        ()
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def update_game(game_id, \
                title ,\
                description,\
                release_date,\
                genre):
    cur = g.cursor()
    cur.execute(
        '''
        update game
        set title=%s ,description=%s,release_date=%s,genre=%s
        where game_id=$s
        ''',
        (title ,description,release_date,genre,game_id)
    )
    
    cur.execute(
        '''
        select * from game where game_id = %s
        ''',
        (game_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def delete_game(game_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from game where game_id=%s
            ''',
            (game_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0

def delete_game_players(game_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from game_player where game_id=%s
            ''',
            (game_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0

def get_game_players(game_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from player where player_id in 
        (select player_id from game_player where game_id=%s)
        ''',
        (game_id)
    )
    ret_dicts = cur.fetchall()

    return ret_dicts

def new_game_player(game_id ,\
            player_id):
    cur = g.cursor()
    cur.execute(
        '''
        insert into game_player
        (game_id,player_id)
        values
        (%s, %s)  
        ''',
        (game_id,player_id)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from game_player where game_player_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict

def is_player_id_existed(player_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from player where player_id=%s
        ''',
        (player_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None

def delete_game_player(game_id, player_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from game_player where game_id=%s and player_id=%s
            ''',
            (game_id,player_id)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0

