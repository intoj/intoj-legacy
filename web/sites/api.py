from flask import *
import json
import db, modules

def Return_JSON(data):
	return Response(json.dumps(data),mimetype='application/json')

def Score_Color():
	if 'score' not in request.args:
		return Return_JSON({
			'success': False,
			'message': 'arg "score" not found'
		})
	if not modules.Is_Integer(request.args['score']):
		return Return_JSON({
			'success': False,
			'message': 'arg "score" is not a integer: %s'%request.args['score']
		})
	score = int(request.args['score'])

	if 'full_score' not in request.args: full_score = 100
	else:
		if not modules.Is_Integer(request.args['full_score']):
			return Return_JSON({
				'success': False,
				'message': 'arg "full_score" is not a integer: %s'%request.args['full_score']
			})
		full_score = int(request.args['full_score'])

	score_color = modules.Score_Color(score,full_score)
	return Return_JSON({
		'success': True,
		'score': score,
		'full_score': full_score,
		'score_color': score_color
	})
