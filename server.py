from nltk.parse.corenlp import CoreNLPServer
import os

java_path = r"C:\Program Files\Java\jdk1.8.0_341\bin\java.exe"
os.environ['JAVA_HOME'] = java_path

STANFORD = os.path.join("models", "stanford-corenlp-4.5.4")

server = CoreNLPServer(
   os.path.join(STANFORD, "stanford-corenlp-4.5.4.jar"),
   os.path.join(STANFORD, "stanford-corenlp-4.5.4-models.jar"),
)

server.start()