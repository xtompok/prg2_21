# Rasterio can open and modify various formats
import rasterio

# Use rasterio.open instead of standard open
# We need to have all files open concurrently because we don't read everything in RAM
with rasterio.open("T32UQA_20220324T100649_B04_10m.jp2") as b04:
    with rasterio.open("T32UQA_20220324T100649_B08_10m.jp2") as b08:
        # Metadata for output is usually get by modification of input metadata
        # Get metadata from b04
        kwargs = b04.meta
        # Change output filetype, data format, number of bands and compression
        kwargs.update(driver="GTiff",dtype=rasterio.float32, count=1, compress='lzw')
        # Print output metadata
        print(kwargs)
        # Open file for writing output and pass metadata to it
        with rasterio.open("ndvi.tiff","w",**kwargs) as out:
            # Read entire b04 data as floats (they are ints in the input file)
            b04data = b04.read(1).astype(float)
            print(b04data)
            # Read entire b08 data as floats
            b08data = b08.read(1).astype(float)
            
            # Output is calculated pixel-wise using formula below
            ndvi = (b08data-b04data) / (b08data+b04data)
            print(b08data)
            # Writing output to file is always done using write_band
            # First argument is index of the band (starting from 1)
            # Second argument is data, here converted to float32 before writing
            out.write_band(1,ndvi.astype(rasterio.float32))
