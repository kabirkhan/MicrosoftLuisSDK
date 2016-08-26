import requests
import json


url = 'https://api.projectoxford.ai/luis/v1/application'

# preview doesn't currently support composite entities which are more important than dialogs'
preview = '/preview'

appid = 'b64e38f3-bb48-49c7-ac06-b8430da76d36'
primary_key = 'b984dc9ba13e49dcbd4752b7bddfe130'
query = 'Can I order 3 slices of pineapple cake'

payload = {'id': appid, 'subscription-key': primary_key, 'q': query}
r = requests.get(url, params = payload)

# json as string
print(r.content)

# pretty printed decoded json
print(json.dumps(r.json(), indent = 4))


class LuisResponse:
    def __init__(self, query = None, intents = None, entities = None, compositeEntities = None, dialog = None):
        self.query = query
        self.intents = intents
        self.entities = entities
        self.compositeEntities = compositeEntities
        self.dialog = dialog
        
class LuisIntent:
    def __init__(self, score = None, intent = None, actions = None):
        self.score = score
        self.intent = intent
        self.actions = actions

class LuisAction:
    def __init__(self, triggered = None, name = None, parameters = None):
        self.triggered = triggered
        self.name = name
        self.parameters = parameters

class LuisActionParameter
    def __init__(self, name = None, required = None, value = None):
        self.name = name
        self.required = required
        self.value = value

class LuisEntity
    def __init__(self, entity = None, type = None, startIndex = None, endIndex = None, score = None):
        self.entity = entity
        self.type = type
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.score = score

class LuisCompositeEntity
    def __init__(self, parentType = None, value = None, children = None):
        self.parentType = parentType
        self.value = value
        self.children = children

class LuisCompositeEntityChild
    def __init__(self, type, value):
        self.type = type
        self.value = value

class LuisDialog
    def __init__(self, prompt, paramterName, contextId, status):
        self.prompt = prompt
        self.parameterName = parameterName
        self.contextId = contextId
        self.status = status