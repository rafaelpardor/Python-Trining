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
xd
  """
  sys.exit(0)


def main():
  global LISTEN
  global PORT
  global EXECUTE
  global COMMAND
  global UPLOAD_DEST
  global TARGET

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

  if not LISTEN and len(TARGET) and PORT > 0:
    buffer = sys.stdin.read()
    client_sender(buffer)

main()









