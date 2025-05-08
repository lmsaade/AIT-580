library(ggplot2)
library(dplyr)

#Read data into RStudio
storm2020 <- read.csv("./decade_data/decade_data/storm_data_2020s.csv",
                  header = TRUE)

#Add record number column
num_rows = nrow(storm2020)
record_num = c(1:num_rows)
storm2020m <- cbind(record_num, storm2020)

#What state had the largest number of instances?
statecount <- head(dplyr::count(storm2020m, STATE, sort = TRUE))
statecount$STATE <- with(statecount, reorder(STATE, -n))
ggplot(statecount, aes(x = STATE, y = n, label = n)) +
  geom_bar(stat = "identity", fill = "#847efb") + 
  geom_text(nudge_y = 1000) +
  theme(legend.position = "none") +
  theme(plot.title = element_text(hjust = 0.5))
#Texas had 27,195 instances of weather events

#What are the top 3 extreme event types for that state?
dftexas <- storm2020m %>% filter(STATE == "TEXAS")
eventcount <- head(dplyr::count(dftexas, EVENT_TYPE, sort = TRUE),3)
eventcount$EVENT_TYPE <- with(eventcount, reorder(EVENT_TYPE, -n))
ggplot(eventcount, aes(x = EVENT_TYPE, y = n, label = n)) +
  geom_bar(stat = "identity", fill  = "#847efb") + 
  geom_text(nudge_y = 400) +
  theme(legend.position = "none") +
  theme(plot.title = element_text(hjust = 0.5))
#Texas' top 3 weather events are hail (6414), drought (4269), and thunderstorm wind (4593)

#When do they typically occur?
top3 = c("Hail", "Drought", "Thunderstorm Wind")
dftop3 <- dftexas %>% filter(EVENT_TYPE %in% top3)
monthcount <- head(dplyr::count(dftop3, MONTH_NAME, sort = TRUE), 3)
monthcount$MONTH_NAME <- with(monthcount, reorder(MONTH_NAME, -n))
ggplot(monthcount, aes(x = MONTH_NAME, y = n, label = n)) +
  geom_bar(stat = "identity", fill  = "#847efb") + 
  geom_text(nudge_y = 200) +
  theme(legend.position = "none") +
  theme(plot.title = element_text(hjust = 0.5))
#Texas' top 3 weather events typically occur in May (4218), April (2821), and June (2074)

#Combine data sources with bind_rows
df1950 <- read.csv("./decade_data/decade_data/storm_data_1950s.csv",
                   header = TRUE)
df1960 <- read.csv("./decade_data/decade_data/storm_data_1960s.csv",
                   header = TRUE)
df1970 <- read.csv("./decade_data/decade_data/storm_data_1970s.csv",
                   header = TRUE)
df1980 <- read.csv("./decade_data/decade_data/storm_data_1980s.csv",
                   header = TRUE)
df1990 <- read.csv("./decade_data/decade_data/storm_data_1990s.csv",
                   header = TRUE)
df2000 <- read.csv("./decade_data/decade_data/storm_data_2000s.csv",
                   header = TRUE)
df2010 <- read.csv("./decade_data/decade_data/storm_data_2010s.csv",
                   header = TRUE)
decades_df <- rbind(df1950, df1960, df1970, df1980, df1990, df2000, df2010, storm2020)

#Texas' event frequency throughout the decades
dftexas2 <- decades_df %>% filter(STATE == "TEXAS")
eventcount2 <- dplyr::count(dftexas2, YEAR, sort = TRUE)
ggplot(eventcount2, aes(x = YEAR, y = n)) +
  geom_line(stat = "identity", color  = "#847efb") + 
  theme(legend.position = "none") +
  theme(plot.title = element_text(hjust = 0.5))
#Texas' event frequency is steadily increasing from 1950s through 2020s