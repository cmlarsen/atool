#! /usr/bin/python

from twitter import *
import argparse

def main():
	token = "3027138436-GMUNK3N4CTH7PcHa40wteJv1TWQhTB0sm4LgSmc"
	token_secret = "5Y4gxVJo6eviqrdiPvbcP64MLCZtLzc1N6SKSJOAHJjIO"
	consumer_key = "TQqkWAzQIbj0w47Fgm7jHac7T"
	consumer_secret = "uRPF5WFCS3shu0l6x8DHJE1GnVHmQWrbac0tAbGq2UUFkJXUWJ"
	
	parser = argparse.ArgumentParser(description="Twitter Logger for A Tool")
	parser.add_argument('-s', '--status', help='Twitter Status', required=True)
	args = parser.parse_args()
	
	print ("Posting Status to Twitter:  %s" % args.status ) 
	
	t = Twitter(
		auth=OAuth(token, token_secret, consumer_key, consumer_secret))
	t.statuses.update(
		status=args.status)

if __name__ == "__main__":
	main()
