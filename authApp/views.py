from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import bcrypt

# Create your views here.

def hash_password(password):
  salt = bcrypt.gensalt()
  hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
  return hash_password

