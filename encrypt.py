import argparse, pyAesCrypt, base64
from pydantic import BaseModel

def add_model(parser, model):
    for name, field in model.model_fields.items():
        parser.add_argument(
            f"--{name}", 
            dest=name,
            type=field.annotation, 
            default=field.default,
        )

class CmdArgs(BaseModel):
    mode: str
    password: str
    input: str
    output: str

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    add_model(parser, CmdArgs)
    args = parser.parse_args()
    cmd = CmdArgs(**vars(args))
    if cmd.mode == "enc":
        pyAesCrypt.encryptFile(cmd.input, cmd.output, cmd.password)
    elif cmd.mode == "dec":
        pyAesCrypt.decryptFile(cmd.input, cmd.output, cmd.password)
    else:
        pass