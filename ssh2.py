import paramiko

def start_connection():
    u_name = 'ericsson'
    pswd = 'Ericsson123#'
    port = 22
    r_ip = '10.219.162.230'
    # sec_key = '/mycert.ppk'

    myconn = paramiko.SSHClient()
    myconn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # my_rsa_key = paramiko.RSAKey.from_private_key_file(sec_key)

    session = myconn.connect(r_ip, username =u_name, password=pswd, port=port)

    remote_cmd = 'ifconfig'
    (stdin, stdout, stderr) = myconn.exec_command(remote_cmd)
    print("{}".format(stdout.read()))
    print("{}".format(type(myconn)))
    print("Options available to deal with the connectios are many like\n{}".format(dir(myconn)))
    myconn.close()


if __name__ == '__main__':
    start_connection()