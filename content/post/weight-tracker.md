---
title: "A Long-term Losing Weight Campaign"
date: 2025-10-20T00:00:00+08:00
lastmod: 2025-10-20T00:00:00+08:00
draft: false
keywords: ["weight loss", "health", "tracking", "fitness"]
description: "Tracking my weight loss journey"
tags: ["Health", "Lifestyle"]
categories: ["Personal"]
author: "Ren Zhenyu"

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: true
toc: true
autoCollapseToc: true
postMetaInFooter: true
hiddenFromHomePage: false
# You can also define another contentCopyright. e.g. contentCopyright: "This is another copyright."
contentCopyright: MIT
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false

# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false

# You can enable or disable out-of-date content warning for individual post.
# Comment this out to use the global config.
#enableOutdatedInfoWarning: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""
typora-copy-images-to: ../../static/weight-tracker.assets
typora-root-url: ../../static
---

# Weight Tracking Record

{{< admonition type=note title="Note" >}}
1. Page content is generated via GPT:) in 5 minutes, which convinces me that AI will let front end enginners lose their jobs, at least.
<!-- 我并不是一个无脑AI吹，我曾经也感觉自己会写代码很牛。但是现在感觉AI时代下，我可能确实需要学习一些不一样的东西了。 -->
(I am not a blind AI supporter. I used to think I was good at coding and proud of it. But now I feel that I may need to learn something different in the age of LLM.)
<br/>
2. Starting from October 20, 2025, I am recording my weight changes with the goal of maintaining healthy weight management.
{{< /admonition >}}


## Data Visualization

<div style="max-width: 900px; margin: 0 auto;">
  <!-- Time Range Selector -->
  <div style="text-align: center; margin-bottom: 20px;">
    <button class="time-range-btn active" data-range="7" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: #4bc0c0; color: white; border-radius: 5px; cursor: pointer; font-weight: bold;">7D</button>
    <button class="time-range-btn" data-range="30" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: transparent; color: #4bc0c0; border-radius: 5px; cursor: pointer; font-weight: bold;">1M</button>
    <button class="time-range-btn" data-range="90" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: transparent; color: #4bc0c0; border-radius: 5px; cursor: pointer; font-weight: bold;">3M</button>
    <button class="time-range-btn" data-range="180" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: transparent; color: #4bc0c0; border-radius: 5px; cursor: pointer; font-weight: bold;">6M</button>
    <button class="time-range-btn" data-range="365" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: transparent; color: #4bc0c0; border-radius: 5px; cursor: pointer; font-weight: bold;">1Y</button>
    <button class="time-range-btn" data-range="all" style="padding: 8px 16px; margin: 0 5px; border: 2px solid #4bc0c0; background: transparent; color: #4bc0c0; border-radius: 5px; cursor: pointer; font-weight: bold;">ALL</button>
  </div>
  <canvas id="weightChart"></canvas>
</div>

<div id="weightStats" style="margin-top: 30px; padding: 20px; background: #f5f5f5; border-radius: 8px;">
  <h3>Statistics</h3>
  <div id="statsContent">Loading...</div>
</div>

## Usage Instructions

Weight data is stored in the `/weight-tracker.assets/weight-data.csv` file with the following format:

```csv
Date,Weight(kg),Notes
2025-10-20,70.0,Starting record
```

To update the data, simply edit the CSV file and add new records.

## Goals and Plans

- 📊 Regularly record weight changes
- 💪 Maintain a healthy lifestyle
- 🎯 Achieve ideal weight goals
- 📅 <font color="red">Push data to github each weekend</font>

---

<style>
.time-range-btn {
  transition: all 0.3s ease;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.time-range-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(75, 192, 192, 0.3);
}

.time-range-btn:active {
  transform: translateY(0);
}

@media (max-width: 600px) {
  .time-range-btn {
    padding: 6px 12px !important;
    font-size: 12px;
    margin: 2px !important;
  }
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js"></script>

<script>
// Global variables
let globalChart = null;
let globalData = [];
let currentRange = 7;

// Helper function: Parse date string to Date object
function parseDate(dateStr) {
  return new Date(dateStr);
}

// Helper function: Format date for display
function formatDate(date, granularity) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  
  if (granularity === 'day') {
    return `${month}-${day}`;
  } else if (granularity === 'week') {
    return `${month}-${day}`;
  } else if (granularity === 'month') {
    return `${year}-${month}`;
  }
  return `${month}-${day}`;
}

// Helper function: Add days to a date
function addDays(date, days) {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
}

// Forward fill missing data (like Apple Watch)
function forwardFillData(data) {
  if (data.length === 0) return [];
  
  const filled = [];
  const startDate = parseDate(data[0].date);
  const endDate = parseDate(data[data.length - 1].date);
  
  let currentDate = new Date(startDate);
  let lastWeight = data[0].weight;
  let dataIndex = 0;
  
  while (currentDate <= endDate) {
    const currentDateStr = currentDate.toISOString().split('T')[0];
    
    // Check if we have data for this date
    if (dataIndex < data.length && data[dataIndex].date === currentDateStr) {
      lastWeight = data[dataIndex].weight;
      filled.push({
        date: currentDateStr,
        weight: lastWeight,
        notes: data[dataIndex].notes,
        isOriginal: true
      });
      dataIndex++;
    } else {
      // Forward fill with last known weight
      filled.push({
        date: currentDateStr,
        weight: lastWeight,
        notes: '',
        isOriginal: false
      });
    }
    
    currentDate = addDays(currentDate, 1);
  }
  
  return filled;
}

// Filter data by time range
function filterDataByRange(data, range) {
  if (range === 'all') return data;
  
  const endDate = parseDate(data[data.length - 1].date);
  const startDate = addDays(endDate, -range);
  
  return data.filter(item => parseDate(item.date) >= startDate);
}

// Determine X-axis granularity based on data length
function getGranularity(dataLength) {
  if (dataLength <= 14) return 'day';
  if (dataLength <= 90) return 'week';
  return 'month';
}

// Aggregate data by granularity
function aggregateData(data, granularity) {
  if (granularity === 'day') return data;
  
  const aggregated = [];
  const groups = {};
  
  data.forEach(item => {
    const date = parseDate(item.date);
    let key;
    
    if (granularity === 'week') {
      // Group by week (every 7 days, show one point)
      const weekNum = Math.floor((date - parseDate(data[0].date)) / (7 * 24 * 60 * 60 * 1000));
      key = weekNum;
    } else if (granularity === 'month') {
      // Group by month
      key = `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}`;
    }
    
    if (!groups[key]) {
      groups[key] = [];
    }
    groups[key].push(item);
  });
  
  // Average weights in each group
  Object.keys(groups).forEach(key => {
    const group = groups[key];
    const avgWeight = group.reduce((sum, item) => sum + item.weight, 0) / group.length;
    const lastItem = group[group.length - 1]; // Use last date in group
    
    aggregated.push({
      date: lastItem.date,
      weight: parseFloat(avgWeight.toFixed(2)),
      notes: lastItem.notes,
      isOriginal: lastItem.isOriginal
    });
  });
  
  return aggregated;
}

// Calculate statistics
function calculateStats(originalData, filteredData) {
  const weights = filteredData.map(item => item.weight);
  const originalWeights = originalData.filter(item => item.isOriginal).map(item => item.weight);
  
  const maxWeight = Math.max(...weights);
  const minWeight = Math.min(...weights);
  const latestWeight = weights[weights.length - 1];
  const startWeight = weights[0];
  const weightChange = latestWeight - startWeight;
  const avgWeight = (weights.reduce((a, b) => a + b, 0) / weights.length).toFixed(2);
  
  return {
    maxWeight,
    minWeight,
    latestWeight,
    startWeight,
    weightChange,
    avgWeight,
    daysRecorded: originalWeights.length,
    totalDays: filteredData.length
  };
}

// Update statistics display
function updateStats(stats) {
  document.getElementById('statsContent').innerHTML = `
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
      <div><strong>🏁 Starting Weight:</strong> ${stats.startWeight} kg</div>
      <div><strong>📍 Current Weight:</strong> ${stats.latestWeight} kg</div>
      <div><strong>📈 Maximum Weight:</strong> ${stats.maxWeight} kg</div>
      <div><strong>📉 Minimum Weight:</strong> ${stats.minWeight} kg</div>
      <div><strong>📊 Average Weight:</strong> ${stats.avgWeight} kg</div>
      <div><strong>🔄 Total Change:</strong> <span style="color: ${stats.weightChange > 0 ? 'red' : 'green'};">${stats.weightChange > 0 ? '+' : ''}${stats.weightChange.toFixed(2)} kg</span></div>
    </div>
    <div style="margin-top: 15px;">
      <strong>📅 Days Recorded:</strong> ${stats.daysRecorded} days 
      <span style="color: #999; margin-left: 10px;">(Total span: ${stats.totalDays} days)</span>
    </div>
  `;
}

// Create or update chart
function updateChart(range) {
  currentRange = range;
  
  // Update button styles
  document.querySelectorAll('.time-range-btn').forEach(btn => {
    if (btn.dataset.range == range) {
      btn.style.background = '#4bc0c0';
      btn.style.color = 'white';
      btn.classList.add('active');
    } else {
      btn.style.background = 'transparent';
      btn.style.color = '#4bc0c0';
      btn.classList.remove('active');
    }
  });
  
  // Filter data
  let filteredData = filterDataByRange(globalData, range);
  
  // Determine granularity
  const granularity = getGranularity(filteredData.length);
  
  // Aggregate data if needed
  const displayData = aggregateData(filteredData, granularity);
  
  // Calculate statistics
  const stats = calculateStats(globalData, filteredData);
  updateStats(stats);
  
  // Prepare chart data
  const dates = displayData.map(item => formatDate(parseDate(item.date), granularity));
  const weights = displayData.map(item => item.weight);
  const remarks = displayData.map(item => item.notes);
  const isOriginal = displayData.map(item => item.isOriginal);
  
  // Detect dark mode
  const isDarkMode = document.getElementById('dark-mode-theme') && 
                     !document.getElementById('dark-mode-theme').disabled;
  
  const textColor = isDarkMode ? '#e0e0e0' : '#666';
  const gridColor = isDarkMode ? 'rgba(255, 255, 255, 0.1)' : 'rgba(0, 0, 0, 0.1)';
  
  // Destroy existing chart
  if (globalChart) {
    globalChart.destroy();
  }
  
  // Create new chart
  const ctx = document.getElementById('weightChart').getContext('2d');
  globalChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dates,
      datasets: [{
        label: 'Weight (kg)',
        data: weights,
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.3,
        fill: true,
        pointRadius: isOriginal.map(orig => orig ? 5 : 3),
        pointHoverRadius: 7,
        pointBackgroundColor: isOriginal.map(orig => orig ? 'rgb(75, 192, 192)' : 'rgba(75, 192, 192, 0.5)'),
        pointBorderColor: '#fff',
        pointBorderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        title: {
          display: true,
          text: `Weight Change Trend (${range === 'all' ? 'All Time' : range + ' Days'})`,
          font: {
            size: 18,
            weight: 'bold'
          },
          color: textColor
        },
        legend: {
          display: true,
          labels: {
            color: textColor
          }
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              const weight = context.parsed.y;
              const original = isOriginal[context.dataIndex];
              return `Weight: ${weight} kg ${original ? '' : '(filled)'}`;
            },
            afterLabel: function(context) {
              const remark = remarks[context.dataIndex];
              return remark ? 'Notes: ' + remark : '';
            }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: 'Weight (kg)',
            color: textColor
          },
          ticks: {
            color: textColor
          },
          grid: {
            color: gridColor
          }
        },
        x: {
          title: {
            display: true,
            text: `Date (${granularity === 'day' ? 'Daily' : granularity === 'week' ? 'Weekly' : 'Monthly'})`,
            color: textColor
          },
          ticks: {
            color: textColor,
            maxRotation: 45,
            minRotation: 45,
            maxTicksLimit: granularity === 'day' ? 30 : granularity === 'week' ? 20 : 12
          },
          grid: {
            color: gridColor
          }
        }
      }
    }
  });
}

// Load and parse CSV data
Papa.parse('/weight-tracker.assets/weight-data.csv', {
  download: true,
  header: true,
  complete: function(results) {
    const rawData = results.data.filter(row => row['Date'] && row['Weight(kg)']);
    
    // Convert to internal format
    const data = rawData.map(row => ({
      date: row['Date'],
      weight: parseFloat(row['Weight(kg)']),
      notes: row['Notes'] || '',
      isOriginal: true
    }));
    
    // Sort by date
    data.sort((a, b) => parseDate(a.date) - parseDate(b.date));
    
    // Forward fill data
    globalData = forwardFillData(data);
    
    // Initial chart with default range
    updateChart(currentRange);
    
    // Add event listeners to buttons
    document.querySelectorAll('.time-range-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const range = this.dataset.range === 'all' ? 'all' : parseInt(this.dataset.range);
        updateChart(range);
      });
    });
  },
  error: function(error) {
    document.getElementById('statsContent').innerHTML = 
      '<p style="color: red;">❌ Unable to load data file. Please ensure weight-data.csv exists.</p>';
    console.error('Error loading CSV:', error);
  }
});
</script>

