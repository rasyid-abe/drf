from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        if 'ErrorDetail' in data['username']:
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data, 'messages': 'Check email to activate your account.'})

        return response
        # import pdb; pdb.set_trace()
        #
        # return super().render(data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)
