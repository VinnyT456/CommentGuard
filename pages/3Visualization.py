import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from wordcloud import WordCloud
from plotly.subplots import make_subplots

st.set_page_config(page_title="Visualization", page_icon="📈")

class YoutubeApp:
    def __init__(self):
        # Initialize the page config and URL for the dataset
        self.url = 'Datasets/Youtube-Spam-Dataset.csv'

    def load_data(self):
        # Load data from the URL
        self.data = pd.read_csv(self.url)

    def prepare_data_visualization(self):
        # Drop unnecessary column and prepare the graph data
        self.graph = self.data.drop("COMMENT_ID",axis=1)
        self.graph = self.graph.dropna(axis=0)
        self.graph['LENGTH'] = self.graph['CONTENT'].apply(lambda x: len(x))
        self.graph['CLASS'] = self.graph['CLASS'].apply(lambda x: "SPAM" if x == 1 else 'NOT SPAM')

    def plot_distribution(self):
        # Create a countplot for Spam Distribution
        spam_count = self.graph[self.graph["CLASS"] == "SPAM"].shape[0]
        not_spam_count = self.graph[self.graph["CLASS"] == "NOT SPAM"].shape[0]
        df = pd.DataFrame({
            "Class": ["NOT SPAM", "SPAM"],
            "Count": [not_spam_count, spam_count]
        })

        fig = px.bar(df,
                    x="Class",
                    y='Count',
                    barmode='group',
                    title='Average Comment Lengths by Spam Classification',
                    labels={"CLASS": "Spam Classification"},
                    color_continuous_scale='picnic',
                    height=600,  # Set height
                    width=2000)  # Set width
        st.plotly_chart(fig, use_container_width=True)

    def plot_box(self):
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Author Name Length by Class", "Comment Length by Class"))
        fig.update_layout(
            width=2000,
            height=800,
            legend=dict(
                title=dict(text="Box Plots"),
            )
        )

        self.graph["AUTHOR_LENGTH"] = self.graph["AUTHOR"].apply(lambda x: len(x))
        fig.add_trace(
            go.Box(x=self.graph["CLASS"],
                   y=self.graph["AUTHOR_LENGTH"],  
                   name="Author Length Plot"
                   ),
            row=1, col=1
        )

        self.graph["LENGTH"] = self.graph["CONTENT"].apply(lambda x: len(x))
        fig.add_trace(
            go.Box(x=self.graph['CLASS'],
                   y=self.graph["LENGTH"],  
                   name="Comment Length Plot"
                   ),
            row=1, col=2
        )

        st.plotly_chart(fig, use_container_width=True)

    def average_comment_length_plot(self):
        df = self.graph.groupby(['CLASS'])["LENGTH"].mean().reset_index(name='Average Length')

        fig = px.bar(df,
                    x="CLASS",
                    y='Average Length',
                    barmode='group',
                    title='Average Comment Lengths by Spam Classification',
                    labels={"CLASS": "Spam Classification"},
                    color_continuous_scale='picnic',
                    height=600,  # Set height
                    width=2000)  # Set width
        st.plotly_chart(fig, use_container_width=True)

    def spam_comment_count_plot(self):
        df = self.graph.groupby(['VIDEO_NAME', 'CLASS']).size().reset_index(name='count')

        fig = px.bar(df,
                    x="VIDEO_NAME",
                    y='count',
                    color="CLASS",
                    barmode='group',
                    title='Spam Comment Counts by Video',
                    labels={"VIDEO_NAME": "Video Name", "count": "Count"},
                    color_continuous_scale='picnic',
                    height=600,  # Set height
                    width=2000)  # Set width
        st.plotly_chart(fig, use_container_width=True)

    def plot_comment_length_by_video(self):
        df = self.graph.groupby(['VIDEO_NAME', 'CLASS'])["LENGTH"].mean().reset_index(name='Average Length')

        fig = px.bar(df,
                    x="VIDEO_NAME",
                    y='Average Length',
                    color="CLASS",
                    barmode='group',
                    title='Average Comment Lengths by Video and Spam Classification',
                    labels={"VIDEO_NAME": "Video Name"},
                    color_continuous_scale='picnic',
                    height=600,  # Set height
                    width=2000)  # Set width
        st.plotly_chart(fig, use_container_width=True)

    def plot_spam_word_cloud(self):
        spam_text = ''.join(self.graph[self.graph["CLASS"] == "SPAM"]["CONTENT"])

        spam_wc = WordCloud(width=1000, height=900, background_color=None, mode="RGBA").generate(spam_text)
        st.image(spam_wc.to_array())
    
    def plot_not_spam_word_cloud(self):
        ham_text = ''.join(self.graph[self.graph["CLASS"] == "NOT SPAM"]["CONTENT"])
        ham_wc = WordCloud(width=1000, height=900, background_color=None, mode="RGBA").generate(ham_text)

        st.image(ham_wc.to_array())

    def plot_time_analysis_comment(self):
        yearly = self.graph[["DATE","CLASS"]].copy()
        yearly["DATE"] = yearly["DATE"].apply(lambda x:x[:4])
        yearly_counts = yearly.groupby(["DATE", "CLASS"]).size().reset_index(name="COUNT")

        monthly = self.graph[["DATE","CLASS"]].copy()
        monthly["DATE"] = monthly["DATE"].apply(lambda x:x[:7])
        monthly_counts = monthly.groupby(["DATE", "CLASS"]).size().reset_index(name="COUNT")

        daily = self.graph[["DATE","CLASS"]].copy()
        daily["DATE"] = daily["DATE"].apply(lambda x:x[:10])
        daily_counts = daily.groupby(["DATE", "CLASS"]).size().reset_index(name="COUNT")

        fig = make_subplots(rows=1, cols=3, subplot_titles=("Daily Spam Comments", "Monthly Spam Comments", "Yearly Spam Comments"), column_widths=[0.4, 0.3, 0.3] )
        fig.update_layout(
            width=100000,
            height=700,
            barmode='group',
        )

        classes = yearly_counts["CLASS"].unique()

        color_map = {
            "SPAM": "crimson",
            "NOT SPAM": "dodgerblue"
        }

        for i in classes:
            yearly_data = yearly_counts[yearly_counts["CLASS"] == i]
            monthly_data = monthly_counts[monthly_counts["CLASS"] == i]
            daily_data = daily_counts[daily_counts["CLASS"] == i]

            fig.add_trace(
                go.Bar(
                    x=daily_data["DATE"],
                    y=daily_data["COUNT"],
                    name=i,
                    legendgroup=i,
                    showlegend=True,
                    marker_color=color_map[i],
                ),
                row=1, col=1
            )

            fig.add_trace(
                go.Bar(
                    x=monthly_data["DATE"],
                    y=monthly_data["COUNT"],
                    name=i,
                    legendgroup=i,
                    showlegend=False,
                    marker_color=color_map[i],
                ),
                row=1, col=2
            )

            fig.add_trace(
                go.Bar(
                    x=yearly_data["DATE"],
                    y=yearly_data["COUNT"],  
                    name=i,
                    legendgroup=i,
                    showlegend=False,
                    marker_color=color_map[i],
                    ),
                row=1, col=3
            )

        fig.update_xaxes(tickangle=-45, row=1, col=1)
        fig.update_xaxes(tickangle=-45, row=1, col=2)
        fig.update_xaxes(tickangle=-45, row=1, col=3)

        st.plotly_chart(fig, use_container_width=True)

    def run(self):
        # Load data and prepare data for visualization
        self.load_data()
        self.prepare_data_visualization()

        page_names_to_funcs = {
            "Spam Distribution Plot": self.plot_distribution,
            "Box Plot": self.plot_box,
            "Average Comment Length Plot": self.average_comment_length_plot,
            "Spam Comment Plot": self.spam_comment_count_plot,
            "Average Comment Length of Videos":self.plot_comment_length_by_video,
            "Spam Comment Word Cloud":self.plot_spam_word_cloud,
            "Not Spam Comment Word Cloud":self.plot_not_spam_word_cloud,
            "Time Analysis of Comments":self.plot_time_analysis_comment, 
        }

        demo_name = st.sidebar.selectbox("Choose a visualization", page_names_to_funcs.keys())
        page_names_to_funcs[demo_name]()


YoutubeApp().run()