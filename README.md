# BGT_2

## Spark with jupyter notebook

docker run -p 8888:8888 jupyter/pyspark-notebook


## Compare
### Local
```
6.228185047999432
Freud most popular words [('the', 131812), ('of', 94372), ('to', 60384), ('a', 46599), ('in', 46310), ('and', 44579), ('that', 33386), ('is', 30321), ('which', 22634), ('it', 22311)]
Freud most popular nouns [('dream', 6042), ('time', 3451), ('analysis', 3372)]
```
### Spark
```
2068906
[('the', 142371), ('of', 94924), ('to', 60988), ('in', 50950), ('a', 48808), ('and', 46208), ('that', 33805), ('is', 30431), ('it', 27788), ('which', 22649)]
[('dream', 6115), ('analysis', 3584), ('time', 3456)]
17.74702417300432
```