import random

import giphy_client

class Giffer:
    async def gif(self, token, args, msg):
        api_instance = giphy_client.DefaultApi()
        api_response = api_instance.gifs_search_get(token,
                                                    args.replace(" ", "+"),
                                                    limit=15, lang='en', fmt='json')
        await msg.channel.send(
            random.choice([d.images.original.url for d in api_response.data]))

    # Utility Methods
    async def puppy(self, token, _, msg): return await self.gif(token, 'puppy', msg) 
    async def boobs(self, token, _, msg): return await self.gif(token, 'boobs', msg) 
    async def kitten(self, token, _, msg): return await self.gif(token, 'kitten', msg) 
    async def four_twenty(self, token, _, msg): return await self.gif(token, '420', msg) 
    async def boo(self, token, _, msg): return await self.gif(token, 'boo', msg) 
    # / Utility Methods





    

        
