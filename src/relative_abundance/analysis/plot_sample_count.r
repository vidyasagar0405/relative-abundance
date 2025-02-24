# Load required packages
library(ggplot2)
library(dplyr)

sample_csv = "./root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal_first.csv"

# Read the CSV file into a data frame
studies <- read.csv("./root:Host-associated:Human:Digestive%20system:Large%20intestine:Fecal_first.csv", stringsAsFactors = FALSE)

# Rename columns for easier use
studies <- studies %>%
  rename(
    study_name = attributes.study.name,
    samples_count = attributes.samples.count
  )

# Convert samples_count to numeric (if not already)
studies$samples_count <- as.numeric(studies$samples_count)

# Plot a horizontal bar graph of all studies
ggplot(studies, aes(x = reorder(study_name, samples_count), y = samples_count)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +  # horizontal bars for better readability
  labs(title = "Samples Count for 320 Studies",
       x = "Study Name",
       y = "Samples Count") +
  theme_minimal() +
  theme(axis.text.y = element_text(size = 6))  # adjust text size as needed


# Filter and sort to get the top 20 studies
top_studies <- studies %>%
  arrange(desc(samples_count)) %>%
  head(20)

# Plot the top 20 studies as a horizontal bar chart
ggplot(top_studies, aes(x = reorder(study_name, samples_count), y = samples_count)) +
  geom_bar(stat = "identity", fill = "tomato") +
  coord_flip() +
  labs(title = "Top 20 Studies by Sample Count",
       x = "Study Name",
       y = "Samples Count") +
  theme_minimal()
