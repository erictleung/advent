library(DBI)
library(readr)
library(dplyr)
library(dbplyr)

con <- dbConnect(RSQLite::SQLite(), dbname = ":memory:")
df <- dbGetQuery(con, statement = read_file('advent2021/01-binary.sql'))


conn <- src_memdb() # create a SQLite database in memory
copy_to(conn,
        storms,     # this is a dataset built into dplyr
        overwrite = TRUE)
tbl(conn, sql("SELECT * FROM storms LIMIT 5"))
dbGetQuery(conn, statement = sql("select * from Persons"))
df <- tibble(a = c(), b = c())
copy_to(conn, df)
