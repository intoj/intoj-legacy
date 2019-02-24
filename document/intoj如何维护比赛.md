# intoj如何维护比赛

---

## 比赛

对于每一场比赛, 系统会分配一个唯一的 **contest_id**

在数据表 contests 内保存了与这个 contest 有关的所有信息, 包括

- 0 id

- 1 标题

- 2 副标题

- 3 开始时间

- 4 结束时间

- 5 描述

- 6 赛制 (json)

- 7 举办者的username

- 8 problems (json)

- 9 admins (json列表) (暂不支持)

### 赛制

赛制可以是:

```json
{
	"type": "oi"
}
```
```json
{
	"type": "icpc",
	"penalty": 20
}
```
```json
{
	"type": "ioi"
}
```
```json
/*
这种赛制与 icpc 赛制有以下不一样的地方:
1. 存在部分分
2. 最终以分数为第一关键字, 总提交次数为第二关键字排序.
请注意即使一道题得到了0分, 依然计算提交次数
*/
{
	"type": "oi-intoj"
}
```

### problems

problems可以是:

```json
// oi赛制下
[
	{
		"id": 2
	},
	{
		"id": 3
	}
]
```
```json
// icpc赛制下
[
	{
		"id": 2,
		"score": 100
	},
	{
		"id": 3,
		"score": 200
	}
]
```
```json
// oi-intoj赛制下:
[
	{
		"id": 2
	},
	{
		"id": 3
	}
]
```

```sql
CREATE TABLE contests(
	id INT NOT NULL PRIMARY KEY auto_increment,
	title VARCHAR(100),
	subtitle VARCHAR(100),
	begin_time VARCHAR(50),
	end_time VARCHAR(50),
	description TEXT,
	rule TEXT,
	holder_name VARCHAR(20),
	problems TEXT,
	admins TEXT
);
```

---

## 比赛参与者

在数据表 contest_players 内保存了与所有参加比赛的人有关的信息, 包括

- 0 id (仅用作主键)

- 1 username

- 2 contest_id

- 3 detail (json)

detail:

```json
[
	{
		"record_id": 10,
		"score": 100,
		"submit_cnt": 1
	},
	{
		"record_id": 11,
		"score": 233,
		"submit_cnt": 100
	}
]
```

```sql
CREATE TABLE contest_players(
	id INT NOT NULL PRIMARY KEY auto_increment,
	username VARCHAR(20),
	contest_id INT,
	detail TEXT
);
```
