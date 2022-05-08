import rasterio
from rasterio.windows import Window

with rasterio.open("T32UQA_20220324T100649_B04_10m.jp2") as b04:
    with rasterio.open("T32UQA_20220324T100649_B08_10m.jp2") as b08:
        kwargs = b04.meta
        kwargs.update(driver="GTiff",dtype=rasterio.float32, count=1, compress='lzw')
        print(kwargs)

        with rasterio.open("ndvi.tiff","w",**kwargs) as out:

            # Processing raster files in blocks speeds up processing time and lowers RAM usage
            # Here we use blocks from b04 file but we can define our own blocks
            for ji, window in b04.block_windows(1):
                # ji is index of the block (starting from (0,0))
                # window is object with stored window size and offset
                print(ji, window)
                # Read only part defined by window
                b04win = b04.read(1,window=window).astype(float)
                b08win = b08.read(1,window=window).astype(float)
                
                # Processing is the same as in blockless operation
                ndvi = (b08win-b04win) / (b08win+b04win)

                # We need to pass window to the writing function so it will know where to write
                out.write_band(1,ndvi.astype(rasterio.float32), window=window)
