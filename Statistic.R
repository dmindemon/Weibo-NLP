comment = read.csv('comment.csv')
str(comment)

# Get the date and hour.
library(lubridate)
return_date = function(string){
    t = string
    md = substr(t,5,10)
    y = substr(t,27,30)
    ymd = paste(y,md)
    ymd = ymd(ymd)
    ymd
}
return_hour = function(string){
    t = string
    h = substr(t,12,13)
    h
}
comment$date = return_date(comment$time)
comment$hour = return_hour(comment$time)
mk_comments = subset(comment, mk==1)
ks_comments = subset(comment, ks==1)

# 1a: Count number of posts and unique users for each brand.
mk_posts = nrow(mk_comments)
ks_posts = nrow(ks_comments)
mk_users = length(unique(mk_comments$user))
ks_users = length(unique(ks_comments$user))

# 1b: Top 10 users and locations.
top_mk_users = sort(table(mk_comments$user),decreasing=T)[1:10]
top_ks_users = sort(table(ks_comments$user),decreasing=T)[1:10]
top_mk_locations = sort(table(mk_comments$province),decreasing=T)[1:10]
top_ks_locations = sort(table(ks_comments$province),decreasing=T)[1:10]

# 2: Find peak day and peak hour.
mk_peak_day = sort(table(mk_comments$date), decreasing=T)[1]
ks_peak_day = sort(table(ks_comments$date), decreasing=T)[1]
mk_peak_hour = sort(table(mk_comments$hour), decreasing=T)[1]
ks_peak_hour = sort(table(ks_comments$hour), decreasing=T)[1]
