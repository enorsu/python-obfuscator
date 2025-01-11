import base64
import sys

print("You have imported shitcode, why?")

class D:
    def decode(a):
        return base64.b64decode(a.encode()).decode()
    
    def encode(a):
        return base64.b64encode(a.encode()).decode()




def decoding(a):
    return f"base64.b64decode('{a}'.encode()).decode()"


global mainstartcode
mainstartcode = f"""
import base64
exec({decoding(D.encode("halal = ''"))})

"""


global shitcode


def argument_validate():
    try:
        global argument_filename
        global argument_output
        argument_filename = sys.argv[1]
        argument_output = sys.argv[2]
        global filename
        
        

        try:
            argument_spamfile = sys.argv[3]
            filename = argument_spamfile
        except IndexError:
        
            filename = "md"

    except IndexError:
        print("Invalid arguments, Usage: python main.py <input> <output> <optional: spamfile name>")
        return
    
    with open(argument_filename, "r") as file:
        wholecode = file.readlines()
        
        
    main(wholecode)
    

def obfuscate(inputfile, outputfile, spamfile):
    global argument_output, filename
    argument_output = outputfile
    filename = spamfile
    with open(inputfile) as x:
        wholecode = x.readlines()

    main(wholecode)

def getBase64Code(b):
    a = f"""
halal += {filename}{b}.skull() + '\\n'
"""
    a = D.encode(a)
    return a


def main(codee):
    code = codee # fuck you i go expldoe
    obf_code = [D.encode(i) for i in code]

    fileopen = open(f"{argument_output}", "w")
    fileopen.write(mainstartcode)


    
    howami = ["{", "}"]
    x = 0
    for i in obf_code:
        x += 1

        


        file = open(f"{filename}{x}.py", "w")
        file.write(f"""import base64             
def skull():
    return f"{howami[0]}base64.b64decode('{i}'.encode()).decode(){howami[1]}"
\n""")
        file.close()

        shit = f"{filename}" + str(x)
        canweputthisinavariable = f"""
exec({decoding(D.encode("import " + shit))})
exec(base64.b64decode('{getBase64Code(x)}'.encode()).decode())

"""
        fileopen.write(canweputthisinavariable)
    
    fileopen.write(f"""
exec({decoding(D.encode("exec(halal)"))})

""")
       







