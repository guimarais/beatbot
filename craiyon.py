from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Photorealistic image of shrek eating earth")
result.save_images() # Saves
