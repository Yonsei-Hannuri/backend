from .DetgoriPdfTextExtracter.DetgoriPdfTextExtracter import DetgoriPdfTextExtracter
from .TextAnalyzer.TextAnalyzer import TextAnalyzer
from .GoogleOauth.GoogleOauth import GoogleOauth
from .ObjectStorage.S3 import S3

detgoriPdfTextExtracter = DetgoriPdfTextExtracter()
textAnalyzer = TextAnalyzer()
googleOauth = GoogleOauth()
objectStorage = S3()
