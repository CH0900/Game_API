# Game_API
### 遊戲服務API範例

#### API 列表

以下是我們設計的遊戲服務API列表：

| API 名稱        | 描述                                      | HTTP 方法 | 路徑                   |
|--------------|-------------------------------------------|----------|------------------------|
| 取得所有遊戲   | 取得所有可用的遊戲列表                      | GET      | /games               |
| 取得單個遊戲   | 根據遊戲ID取得遊戲詳細信息                | GET      | /games/{game_id}     |
| 創建新遊戲    | 創建一個新的遊戲                            | POST     | /games               |
| 更新遊戲資訊  | 根據遊戲ID更新遊戲的資訊                    | PUT      | /games/{game_id}     |
| 刪除遊戲      | 根據遊戲ID刪除遊戲                        | DELETE   | /games/{game_id}     |
| 取得遊戲玩家   | 根據遊戲ID取得遊戲內的玩家列表              | GET      | /games/{game_id}/players |
| 加入遊戲玩家   | 根據遊戲ID將玩家添加到遊戲中                | POST     | /games/{game_id}/players |
| 移除遊戲玩家   | 根據遊戲ID從遊戲中移除玩家                | DELETE   | /games/{game_id}/players/{player_id} |

#### 資料表格與欄位

我們將使用以下資料表格來支持遊戲服務API：

1. Game (遊戲) 資料表格：

   - game_id (遊戲ID) - 主鍵
   - title (遊戲標題)
   - description (遊戲描述)
   - release_date (遊戲發佈日期)
   - genre (遊戲類型)

2. Player (玩家) 資料表格：

   - player_id (玩家ID) - 主鍵
   - username (玩家用戶名)
   - email (玩家電子郵件)
   - registration_date (註冊日期)

3. GamePlayer (遊戲玩家) 資料表格：

   - game_player_id (遊戲玩家ID) - 主鍵
   - game_id (遊戲ID) - 外鍵關聯到Game資料表格
   - player_id (玩家ID) - 外鍵關聯到Player資料表格
