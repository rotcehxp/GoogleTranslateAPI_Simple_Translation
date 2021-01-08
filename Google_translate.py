#Google Translate
#Built with Google Translation tools

from googleapiclient.discovery import build
#html is used to avoid any problem with special characters
import html

#Google Translate needs at least three values to return a result
#"developerKey", "q", in this case I used "text"; and "target", that
#that is the abbrevation of the language we want to translate to
def g_translate(text,targetlanguage):
    service = build('translate', 'v2',developerKey='YOUR API')
    request = service.translations().list(q=text, target=targetlanguage)
    response = request.execute()
    return response['translations'][0]['translatedText']

text='Trying to use Google Translate!'
targetlanguage="spa"
result = g_translate(text,targetlanguage)
#simple parser to avoid special character problems
print("result:", html.unescape(result))


