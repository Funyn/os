#coding:utf-8
from hashlib import md5

db = {
    'michael': 'b86398db4df65fc388ac1f7239152aee',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def get_md5(value):
	md = md5()
	md.update(str(value).encode('utf8'))
	return md.hexdigest()

def calc_md5(password,username):
	return get_md5(str(password)+str(username)+'yourneverguess')

def login(user,password):
	have_user = db.get(user,None)
	if not have_user:
		return '该用户不存在'
	password = calc_md5(password,user)
	print(password)
	if db[user] == password:
		return True
	else:
		return False
