import rasterio
from rasterio.windows import Window

with rasterio.open("T32UQA_20220324T100649_B04_10m.jp2") as b04:
	with rasterio.open("T32UQA_20220324T100649_B08_10m.jp2") as b08:
		kwargs = b04.meta
		kwargs.update(driver="GTiff",dtype=rasterio.float32, count=1, compress='lzw')
		print(kwargs)

		with rasterio.open("ndvi.tiff","w",**kwargs) as out:

			for ji, window in b04.block_windows(1):
				print(ji, window)
				b04win = b04.read(1,window=window).astype(float)
				b08win = b08.read(1,window=window).astype(float)
				
				ndvi = (b08win-b04win) / (b08win+b04win)

				out.write_band(1,ndvi.astype(rasterio.float32), window=window)
