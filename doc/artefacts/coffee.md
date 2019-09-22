1. Order BC 會從 Barista BC 取得咖啡列表
2. Order BC 建立訂單後，會丟給 Barista 執行訂單，但如果 Barista 發現冰箱庫存不足，則該訂單失效
3. Inventory Item 加入保存期限概念，所以 Inventory Item 從 Value Object 升級成 Aggregate Root
4. Barista 會有一支 api 讓使用者向 inventory 進貨