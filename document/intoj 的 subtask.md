```json
{
	"subtasks": [
		{
			"id": 1,
			"cases": [
				{ "id":1, "status": 10, "score": 80, "checker_message": "OK", "judger_message": "ac", "time_usage": 10, "memory_usage": 20 },
				{ "id":2, "status": 9, "score": 80, "checker_message": "OK", "judger_message": "", "time_usage": 10, "memory_usage": 20 },
				{ "id":3, "status": 8, "score": 80, "checker_message": "OK", "judger_message": "", "time_usage": 10, "memory_usage": 20 }
			],
			"full_score": 2,
			"score": 10,
			"time_usage": 100,
			"memory_usage": 256,
			"status": 8
		},
		{
			"id": 2,
			"cases": [
				{ "id":1, "status": 7, "score": 80, "checker_message": "OK", "judger_message": "clone", "time_usage": 10, "memory_usage": 20 },
				{ "id":2, "status": 6, "score": 80, "checker_message": "OK", "judger_message": "", "time_usage": 10, "memory_usage": 20 },
				{ "id":3, "status": 6, "score": 80, "checker_message": "OK", "judger_message": "", "time_usage": 10, "memory_usage": 20 }
			],
			"full_score": 20,
			"score": 0,
			"time_usage": 1,
			"memory_usage": 19,
			"status": 6
		},
		{
			"id": 3,
			"cases": [
				{ "id":1, "status": 10, "score": 80, "checker_message": "OK", "judger_message": "orztyx", "time_usage": 10, "memory_usage": 20 },
				{ "id":2, "status": 10, "score": 80, "checker_message": "OK", "judger_message": "orzzyy", "time_usage": 10, "memory_usage": 20 },
				{ "id":3, "status": 10, "score": 80, "checker_message": "OK", "judger_message": "orzcy", "time_usage": 10, "memory_usage": 20 }
			],
			"full_score": 40,
			"score": 40,
			"time_usage": 200,
			"memory_usage": 256,
			"status": 10
		}
	]
}
```

注意! full_score 为 **每个测试点** 的满分!

```json
{
	"subtasks": [
		{
			"time_limit": 1000,
			"memory_limit": 256,
			"input_file": "dat[1,2]-.*\\.in",
			"score": 2333
		}
	],
	"special_judge": {
		"filename": "spj.cpp",
		"language": "cpp17"
	}
}
```
