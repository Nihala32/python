# sentiment analysis algorithm

# tokanization step(rvw to token)

# positive dict
# negative dic

# token compare with dic
# if token is positive dic word then assign value 1
# if words are nutrel pass value 0

# count
# final output plus value=positive count

df['sentimentt'] = df['sentiment'].replace({-1 : 'negative'})
df['sentimentt'] = df['sentimentt'].replace({1 : 'positive'})
fig = px.histogram(df, x="sentimentt")
fig.update_traces(marker_color="indianred",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Product Sentiment')
fig.show(



