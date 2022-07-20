import sys
 
# Save the current stdout so that we can revert sys.stdou after we complete
# our redirection
stdout_fileno = sys.stdout
 
sample_input = sys.stdin
 
# Redirect sys.stdout to the file
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')
for ip in sample_input:
    # Prints to the redirected stdout (Output.txt)
    print('HELLO')
    print(ip)
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    sys.stdout.write(ip + '\n')
    # Prints to the actual saved stdout handler
    stdout_fileno.write(ip + '\n')
 
# Close the file
sys.stdout.close()
# Restore sys.stdout to our old saved file handler
sys.stdout = stdout_fileno

#https://www.askpython.com/python/python-stdin-stdout-stderr