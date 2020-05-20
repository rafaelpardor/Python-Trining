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


def server_loop():
  global TARGET

  # if no target is defined, we kusten in all interfaces
  if not len(TARGET):
    TARGET = "0.0.0.0"

  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((TARGET, PORT))
  server.listen(5)

  while True:
    client_socket, addr = server.accept()

    # sping off a thread to handle our new client
    client_thread = threading.Thread(
        target=client_handler, args=(client_socket,)
        )
    client_thread.start()

def run_command(command):
  # trim the newline
  command = command.rstrip()

  # run the command and get the output back
  try:
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
  except:
    output = "Failed to exceute command \r\n"

  # send the output back to the client
  return output

def client_handler(client_socket):
  global UPLOAD
  global EXECUTE
  global COMMAND

  # check for upload
  if len(UPLOAD_DEST):
    # read in all of the bytes and write to our destination
    file_buffer = ""

    # keep reading data until none is available
    while True:
      data = client_socket.recv(1024)

      if not data:
        break
    else:
        file_buffer =+ data

    # now we take these bytes and try to write them out
    try:
      file_descriptor = open(UPLOAD_DEST, "wb")
      file_descriptor.write(file_buffer)
      file_descriptor.close()

      # acknowldege that we wrote the file out
      client_socket.send("Successfully saved file to %s\r\n" % UPLOAD_DEST)
    except:
      client_socket.send("failed to save file %s\r\n" % UPLOAD_DEST)

    # check for command execution
    if len(EXECUTE):
      # run the command
      output = run_command(execute)

      client_socket.send(output)

    # now we go into another loop if a command shell was requested
    if COMMAND:
      while True:
        # show a simple prompt
        client_socket.send("<BHP:#?")
        cmd_buffer = ""
        while "\n" not in cmd_buffer:
          cmd_buffer =+ client_socket.recv(1024)

        # send back the command output
        response = run_command(cmd_buffer)

        #send back the response
        client_socket.send(response)

main()
