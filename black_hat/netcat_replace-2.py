import sys
import socket
import getopt
import threading
import subprocess

# define some goals variables
LISTEN = False
COMMAND = False
UPLOAD = False
EXECUTE = ""
TARGET = ""
UPLOAD_DEST = ""
PORT = 0


def usage():
  print """------Netcat replacer------

Usage: netcat_replace.py -t target_host -p port
-l --listen               - listen on [host]:[port] for
                            incoming connection

-e --execute-file_to_run  - execute the given file upon

-c --command              - Initialize a command shell

-u --upload               - upon receiving connection upload a
                            file and write destination
  """
  sys.exit(0)


def main():
  global LISTEN
  global PORT
  global EXECUTE
  global COMMAND
  global UPLOAD_DEST
  global TARGET

  # if theres no arguments, usage()
  if not len(sys.argv[1:]):
    usage()

  # read the command line options
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
    ["help", "listen", "execute", "target", "port", "command", "upload"])
  except getopt.GetoptError as err:
    print str(err)
    usage()

  for o, a in opts:
    if o in ("-h", "--help"):
      usage()
    elif o in ("-l", "--listen"):
      LISTEN = True
    elif o in ("-e", "--execute"):
      EXECUTE = a
    elif o in ("-c", "--commamd"):
      COMMAND = True
    elif o in ("-u", "--upload"):
      UPLOAD_DEST = a
    elif o in ("-t", "--target"):
      TARGET = a
    elif o in ("-p", "--port"):
      PORT = int(a)
    else:
      assert False, "ungandled option"

  # are we going to listen or just send data from stdin?
  if not LISTEN and len(TARGET) and PORT > 0:
    # read in the buffer from the command line
    # this whill block, so send CTRL-D if not sending input
    # to stdin
    buffer = sys.stdin.read()

    # send data off
    client_sender(buffer)

  # we are going to listen and potentially
  # upload things, execute commands, and drop a shell back
  # depending on our command line options abovr
  if LISTEN:
    server_loop()


def client_sender(buffer):
  clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    # connect to our target host
    client.connect((target, port))

    if len(buffer):
      client.send(buffer)
    while True:
      recv_len = 1
      response = ""

      while recv_len:
        data = client.recv(4096)
        recv_len = len(data)
        response += data

        if recv_len < 4096:
          break

      print response,

      # wait for mor input
      buffer = raw_input("")
      buffer += "\n"

      # send it off
      client.send(buffer)

  except:
    print "[*] Exception Exiting"

    # tear down the connection
    client.close()


main()
