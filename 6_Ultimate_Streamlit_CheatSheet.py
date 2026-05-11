# Ultimate Streamlit Cheat Sheet

> **Version:** 2026 Edition | **Covers:** Streamlit 1.40+ | **Format:** Clean Markdown Tables
> **Optimized for:** GitHub, VS Code, Jupyter, and any markdown viewer

---

## Table of Contents

1. [Install, Import & CLI](#1-install-import--cli)
2. [Text & Typography](#2-text--typography)
3. [Data Display](#3-data-display)
4. [Input Widgets](#4-input-widgets)
5. [Media Elements](#5-media-elements)
6. [Charts & Visualizations](#6-charts--visualizations)
7. [Layout & Containers](#7-layout--containers)
8. [Status, Progress & Feedback](#8-status-progress--feedback)
9. [Control Flow](#9-control-flow)
10. [Session State](#10-session-state)
11. [Caching](#11-caching)
12. [Navigation & Multi-Page Apps](#12-navigation--multi-page-apps)
13. [Forms, Dialogs & Fragments](#13-forms-dialogs--fragments)
14. [Deployment & Terminal Commands](#14-deployment--terminal-commands)
15. [Common Patterns & How to Interpret Results](#15-common-patterns--how-to-interpret-results)

---

## 1. Install, Import & CLI

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Install** | `pip install streamlit` | Install Streamlit from PyPI | `pip install streamlit` |
| **Nightly** | `pip install streamlit-nightly` | Install pre-release features | `pip uninstall streamlit && pip install streamlit-nightly --upgrade` |
| **Import** | `import streamlit as st` | Standard import convention | `import streamlit as st` |
| **Run App** | `streamlit run` | Launch app in browser from terminal | `streamlit run app.py` |
| **Hello Demo** | `streamlit hello` | Launch built-in demo app | `streamlit hello` |
| **Show Config** | `streamlit config show` | Display current configuration | `streamlit config show` |
| **Clear Cache** | `streamlit cache clear` | Clear all cached data | `streamlit cache clear` |
| **Show Version** | `streamlit version` | Display Streamlit version | `streamlit version` |
| **Show Help** | `streamlit help` | Display CLI help | `streamlit help` |
| **Open Docs** | `streamlit docs` | Open documentation in browser | `streamlit docs` |
| **Init Project** | `streamlit init` | Initialize a new Streamlit project | `streamlit init` |

### How to Open & Access the App

```bash
# 1. Open terminal / command prompt
# 2. Navigate to your project folder
cd /path/to/your/project

# 3. Run the app
streamlit run app.py

# 4. Terminal output looks like:
#   You can now view your Streamlit app in your browser.
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.5:8501

# 5. Open your browser and go to:
#   http://localhost:8501

# 6. To stop the app, press CTRL+C in the terminal
```

**Two-Screen Workflow:**
- **Screen 1 (Terminal):** Shows logs, errors, and the running server. Keep this open.
- **Screen 2 (Browser):** Displays the interactive app at `http://localhost:8501`. Auto-refreshes on file save.

---

## 2. Text & Typography

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Magic Write** | *implicit* | Any string/variable at top level calls `st.write()` | `"Hello World"` or `my_df` or `["st", "is <", 3]` |
| **Write** | `st.write()` | Universal display: text, data, charts, objects | `st.write("Hello", my_df, fig)` |
| **Write Stream** | `st.write_stream()` | Stream generator output (e.g., LLM tokens) | `st.write_stream(my_generator)` |
| **Text** | `st.text()` | Fixed-width plain text | `st.text("Fixed width text")` |
| **Markdown** | `st.markdown()` | Render Markdown with HTML support | `st.markdown("**Bold** and _Italic_")` |
| **LaTeX** | `st.latex()` | Render mathematical expressions | `st.latex(r"e^{i\pi} + 1 = 0")` |
| **Title** | `st.title()` | Large page title | `st.title("My Awesome App")` |
| **Header** | `st.header()` | Section header | `st.header("Section 1")` |
| **Subheader** | `st.subheader()` | Sub-section header | `st.subheader("Subsection A")` |
| **Code Block** | `st.code()` | Display syntax-highlighted code | `st.code("for i in range(10): print(i)", language='python')` |
| **Badge** | `st.badge()` | Display a small status badge | `st.badge("New", icon=":material/star:")` |
| **HTML** | `st.html()` | Render raw HTML | `st.html("<p style='color:red;'>Red text</p>")` |
| **iFrame** | `st.iframe()` | Embed external web pages | `st.iframe("https://docs.streamlit.io", height=600)` |
| **Caption** | `st.caption()` | Small italic caption text | `st.caption("Data source: Kaggle 2024")` |
| **Divider** | `st.divider()` | Horizontal separator line | `st.divider()` |
| **Echo** | `st.echo()` | Display code and execute it | `with st.echo(): df.head()` |

---

## 3. Data Display

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **DataFrame** | `st.dataframe()` | Interactive scrollable DataFrame | `st.dataframe(df, use_container_width=True, hide_index=True)` |
| **Data Editor** | `st.data_editor()` | Editable DataFrame widget | `st.data_editor(df, num_rows="dynamic", key="editor")` |
| **Static Table** | `st.table()` | Static full-width table | `st.table(df.iloc[:10])` |
| **JSON** | `st.json()` | Pretty-print JSON/dict | `st.json({"name": "Alice", "age": 30})` |
| **Metric** | `st.metric()` | KPI card with delta indicator | `st.metric("Revenue", "$12,450", delta="+8.5%", delta_description="vs last month")` |
| **Column Metric** | `st.columns` + `st.metric` | Side-by-side KPI cards | `cols = st.columns(3); cols[0].metric("A", 100); cols[1].metric("B", 200)` |
| **Dict/Obj** | `st.write()` | Auto-detects and displays dicts/lists | `st.write({"key": "value", "list": [1,2,3]})` |

**Interpreting `st.data_editor` Results:**
```python
# After user edits, access changes via session state
st.data_editor(df, key="my_editor")
st.write(st.session_state["my_editor"])
# Returns: {"edited_rows": {0: {"col": "new_val"}}, "added_rows": [...], "deleted_rows": [...]}
```

---

## 4. Input Widgets

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Button** | `st.button()` | Momentary trigger; returns `True` on click only | `if st.button("Submit", type="primary", icon=":material/check:"): st.write("Clicked!")` |
| **Checkbox** | `st.checkbox()` | Persistent boolean toggle | `agree = st.checkbox("I agree", value=False)` |
| **Toggle** | `st.toggle()` | On/off switch (modern checkbox) | `dark_mode = st.toggle("Dark Mode", value=False)` |
| **Radio** | `st.radio()` | Single-select from list | `choice = st.radio("Pick one", ["A", "B", "C"], horizontal=True)` |
| **Selectbox** | `st.selectbox()` | Dropdown single-select | `option = st.selectbox("Choose", df["col"].unique(), index=0)` |
| **Multiselect** | `st.multiselect()` | Dropdown multi-select | `options = st.multiselect("Select fruits", ["Apple", "Banana", "Cherry"], default=["Apple"])` |
| **Slider** | `st.slider()` | Numeric range slider | `age = st.slider("Age", 0, 100, 25)` |
| **Range Slider** | `st.slider()` | Dual-handle range selector | `range_val = st.slider("Range", 0.0, 100.0, (25.0, 75.0))` |
| **Select Slider** | `st.select_slider()` | Slider with discrete options | `size = st.select_slider("Size", ["S", "M", "L", "XL"], value="M")` |
| **Number Input** | `st.number_input()` | Numeric text entry with +/- | `num = st.number_input("Enter a number", min_value=0, max_value=100, value=50, step=5)` |
| **Text Input** | `st.text_input()` | Single-line text entry | `name = st.text_input("Name", placeholder="Enter your name", max_chars=50)` |
| **Text Area** | `st.text_area()` | Multi-line text entry | `bio = st.text_area("Bio", height=150, max_chars=500)` |
| **Date Input** | `st.date_input()` | Date picker | `date = st.date_input("Birthdate", value=datetime.date(2000, 1, 1))` |
| **Time Input** | `st.time_input()` | Time picker | `time = st.time_input("Meeting time", value=datetime.time(9, 0))` |
| **Color Picker** | `st.color_picker()` | Hex color selector | `color = st.color_picker("Pick a color", "#FF4B4B")` |
| **File Uploader** | `st.file_uploader()` | Upload files from user | `file = st.file_uploader("Upload CSV", type=["csv", "xlsx"], accept_multiple_files=False)` |
| **Camera Input** | `st.camera_input()` | Capture photo from webcam | `photo = st.camera_input("Take a photo")` |
| **Chat Input** | `st.chat_input()` | Chat-style text input | `prompt = st.chat_input("Ask me anything...")` |

**Interpreting Button Results:**
```python
# st.button() returns True ONLY on the rerun caused by the click
# It immediately becomes False on the next rerun
# For persistence, use session state or callbacks

if st.button("Process"):
    st.write("Processing...")  # Shows only momentarily

# BETTER: Use session state for persistence
if "processed" not in st.session_state:
    st.session_state.processed = False
if st.button("Process"):
    st.session_state.processed = True
if st.session_state.processed:
    st.write("Done!")  # Persists until explicitly cleared
```

---

## 5. Media Elements

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Image** | `st.image()` | Display images (PNG, JPG, SVG, GIF) | `st.image("photo.png", caption="My photo", width=300, link="https://example.com")` |
| **Logo** | `st.logo()` | Display app logo in sidebar | `st.logo("logo.png", icon_image="icon.png")` |
| **Audio** | `st.audio()` | Play audio files or bytes | `st.audio("song.mp3", format="audio/mp3", start_time=10)` |
| **Video** | `st.video()` | Play video files or URLs | `st.video("movie.mp4", subtitles="./subs.vtt", loop=True, autoplay=False)` |
| **PDF** | `st.pdf()` | Embed PDF documents | `st.pdf("report.pdf", width=700)` |

---

## 6. Charts & Visualizations

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Line Chart** | `st.line_chart()` | Simple native line chart | `st.line_chart(df[["col1", "col2"]])` |
| **Area Chart** | `st.area_chart()` | Stacked area chart | `st.area_chart(df[["a", "b", "c"]])` |
| **Bar Chart** | `st.bar_chart()` | Vertical bar chart | `st.bar_chart(df.set_index("category")["value"])` |
| **Map** | `st.map()` | Scatter map with lat/lon | `st.map(df, latitude="lat", longitude="lon", size="population", color="category")` |
| **Pyplot** | `st.pyplot()` | Display Matplotlib figures | `fig, ax = plt.subplots(); ax.plot(x, y); st.pyplot(fig)` |
| **Altair** | `st.altair_chart()` | Display Altair charts | `st.altair_chart(chart, use_container_width=True)` |
| **Plotly** | `st.plotly_chart()` | Display Plotly figures | `st.plotly_chart(fig, use_container_width=True)` |
| **Bokeh** | `st.bokeh_chart()` | Display Bokeh figures | `st.bokeh_chart(fig, use_container_width=True)` |
| **PyDeck** | `st.pydeck_chart()` | Display PyDeck/Deck.gl maps | `st.pydeck_chart(pydeck_obj)` |
| **Graphviz** | `st.graphviz_chart()` | Display Graphviz diagrams | `st.graphviz_chart('digraph {A -> B}')` |
| **Vega-Lite** | `st.vega_lite_chart()` | Display Vega-Lite specs | `st.vega_lite_chart(df, spec={"mark": "line", "encoding": {...}})` |

---

## 7. Layout & Containers

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Sidebar** | `st.sidebar` | Left navigation panel for controls | `st.sidebar.title("Controls"); st.sidebar.selectbox("Filter", options)` |
| **Columns** | `st.columns()` | Horizontal column layout | `col1, col2, col3 = st.columns([1, 2, 1]); col1.write("Left")` |
| **Tabs** | `st.tabs()` | Tabbed content containers | `tab1, tab2 = st.tabs(["Chart", "Data"]); tab1.line_chart(df)` |
| **Expander** | `st.expander()` | Collapsible content section | `with st.expander("Show details", icon=":material/info:"): st.write("Hidden content")` |
| **Popover** | `st.popover()` | Floating button-triggered container | `with st.popover("Settings"): st.checkbox("Enable")` |
| **Container** | `st.container()` | Invisible bounding box for grouping | `with st.container(border=True): st.write("Boxed content")` |
| **Empty** | `st.empty()` | Placeholder for dynamic content | `placeholder = st.empty(); placeholder.write("Loading..."); placeholder.write("Done!")` |
| **Chat Message** | `st.chat_message()` | Chat UI bubble (user/assistant) | `with st.chat_message("user"): st.write("Hello")` |
| **Status** | `st.status()` | Expandable process status container | `with st.status("Processing...", expanded=True) as s: s.update(label="Done!")` |

**Interpreting Layout Results:**
```python
# Columns return proportional widths based on the list provided
col1, col2 = st.columns([1, 3])  # col2 is 3x wider than col1
# Tabs return container objects; use 'with' notation or dot notation
tab1, tab2 = st.tabs(["A", "B"])
with tab1:
    st.write("Content A")
tab2.write("Content B")  # Equivalent dot notation
```

---

## 8. Status, Progress & Feedback

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Spinner** | `st.spinner()` | Loading indicator during execution | `with st.spinner("Loading data..."): time.sleep(2); st.success("Done!")` |
| **Progress** | `st.progress()` | Progress bar (0-100) | `bar = st.progress(0); for i in range(100): bar.progress(i+1)` |
| **Success** | `st.success()` | Green success message box | `st.success("Operation completed successfully!")` |
| **Info** | `st.info()` | Blue informational message | `st.info("This is a helpful tip.")` |
| **Warning** | `st.warning()` | Orange warning message | `st.warning("Check your input before proceeding.")` |
| **Error** | `st.error()` | Red error message | `st.error("An error occurred while processing.")` |
| **Exception** | `st.exception()` | Display exception traceback | `st.exception(e)` |
| **Toast** | `st.toast()` | Brief popup notification | `st.toast("File saved!", icon="👍")` |
| **Balloons** | `st.balloons()` | Celebration animation | `st.balloons()` |
| **Snow** | `st.snow()` | Snowflake animation | `st.snow()` |

---

## 9. Control Flow

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Stop** | `st.stop()` | Halt script execution immediately | `if not password: st.warning("Login required"); st.stop()` |
| **Rerun** | `st.rerun()` | Force immediate script rerun | `if st.button("Refresh"): st.rerun()` |
| **Switch Page** | `st.switch_page()` | Navigate to another page file | `st.switch_page("pages/dashboard.py")` |
| **Page Link** | `st.page_link()` | Create navigation link to a page | `st.page_link("pages/help.py", label="Help", icon="🛟")` |
| **Fragment** | `@st.fragment` | Partial rerun without full reload | `@st.fragment def my_widget(): st.button("Update")` |
| **Form** | `st.form()` | Batch widget submissions | `with st.form("my_form"): name = st.text_input("Name"); st.form_submit_button("Submit")` |
| **Dialog** | `@st.dialog()` | Modal popup window | `@st.dialog("Confirm") def confirm(): st.write("Are you sure?")` |

---

## 10. Session State

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Initialize** | `st.session_state` | Persistent dict across reruns per user | `if "count" not in st.session_state: st.session_state.count = 0` |
| **Read** | `st.session_state.key` | Access stored value | `st.write(st.session_state.count)` |
| **Write** | `st.session_state.key = val` | Store or update value | `st.session_state.count = 5` |
| **Delete** | `del st.session_state.key` | Remove key from state | `del st.session_state.count` |
| **Callback** | `on_click` / `on_change` | Trigger function on widget interaction | `st.button("Inc", on_click=increment, args=(1,))` |
| **Query Params** | `st.query_params` | Read/write URL parameters | `st.query_params["page"] = "home"; st.query_params.clear()` |
| **Context** | `st.context` | Access browser cookies, headers, locale | `st.write(st.context.cookies); st.write(st.context.headers)` |

**Interpreting Session State:**
```python
# Session state persists across reruns FOR EACH USER independently
# Other users do NOT see your session state values
# Use it to store: form data, login state, UI preferences, cached user results

# Pattern: Initialize once, read/update many times
if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("data.csv")

# Pattern: Callback to modify state cleanly
def increment():
    st.session_state.counter += 1
st.button("+", on_click=increment)
st.write(f"Count: {st.session_state.counter}")
```

---

## 11. Caching

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Cache Data** | `@st.cache_data` | Cache serializable data (DataFrames, lists) | `@st.cache_data def load_data(url): return pd.read_csv(url)` |
| **Cache Resource** | `@st.cache_resource` | Cache non-serializable objects (models, DB connections) | `@st.cache_resource def load_model(): return pipeline("sentiment-analysis")` |
| **Clear Data Cache** | `st.cache_data.clear()` | Clear specific data cache | `@st.cache_data.clear()` |
| **Clear Resource Cache** | `st.cache_resource.clear()` | Clear specific resource cache | `@st.cache_resource.clear()` |
| **TTL** | `ttl` parameter | Time-to-live for cache expiration | `@st.cache_data(ttl=3600) def fetch(): return requests.get(url).json()` |
| **Max Entries** | `max_entries` parameter | Limit cache size (LRU eviction) | `@st.cache_data(max_entries=100) def process(x): return x**2` |
| **Persist** | `persist` parameter | Disk persistence option | `@st.cache_data(persist="disk") def heavy_compute(): ...` |
| **Show Spinner** | `show_spinner` parameter | Show loading during cache miss | `@st.cache_data(show_spinner=False) def load(): ...` |

**Interpreting Caching Results:**
```python
# @st.cache_data: Result is shared across ALL users and sessions
# Use for: Data loading, expensive computations, API calls
# Input arguments must be hashable

# @st.cache_resource: Object is shared across ALL users (singleton pattern)
# Use for: ML models, database connections, heavy initialization
# Do NOT mutate cached resources without considering thread safety

# Cache is invalidated when: function code changes, arguments change, or manually cleared
```

---

## 12. Navigation & Multi-Page Apps

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Page Object** | `st.Page()` | Define a page for navigation | `page = st.Page("page1.py", title="Home", icon=":material/home:", default=True)` |
| **Navigation** | `st.navigation()` | Create sidebar navigation menu | `pg = st.navigation([st.Page("home.py"), st.Page("about.py")]); pg.run()` |
| **Grouped Nav** | `st.navigation()` with dict | Grouped pages with section headers | `pg = st.navigation({"Account": [login], "Analytics": [dash, reports]}); pg.run()` |
| **Page Link** | `st.page_link()` | Inline link to another page | `st.page_link("pages/help.py", label="Help Center", icon="🛟")` |
| **Switch Page** | `st.switch_page()` | Programmatic page navigation | `st.switch_page("pages/settings.py")` |
| **Hidden Pages** | `visibility` param | Hide from nav but keep routable | `st.Page("admin.py", title="Admin", visibility="hidden")` |

**Interpreting Navigation Results:**
```python
# File structure for multipage apps:
# project/
#   streamlit_app.py   (entry point)
#   pages/
#     dashboard.py
#     settings.py
#
# In streamlit_app.py:
pg = st.navigation([
    st.Page("streamlit_app.py", title="Home"),
    st.Page("pages/dashboard.py", title="Dashboard"),
    st.Page("pages/settings.py", title="Settings")
])
pg.run()  # MUST call .run() to execute the selected page
```

---

## 13. Forms, Dialogs & Fragments

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Form** | `st.form()` | Group widgets; submit all at once | `with st.form("login"): u = st.text_input("User"); p = st.text_input("Pass"); st.form_submit_button("Login")` |
| **Form Submit** | `st.form_submit_button()` | Trigger form submission | `submitted = st.form_submit_button("Submit", type="primary")` |
| **Dialog** | `@st.dialog()` | Modal popup with overlay | `@st.dialog("Delete?") def confirm(): if st.button("Yes"): st.session_state.deleted = True` |
| **Fragment** | `@st.fragment()` | Independent rerun section | `@st.fragment def chart_widget(): st.line_chart(get_data()); st.button("Refresh")` |
| **Popover** | `st.popover()` | Button-triggered floating panel | `with st.popover("Filters"): st.multiselect("Categories", [...])` |

**Interpreting Form Results:**
```python
# Widgets inside a form do NOT trigger reruns when changed
# Only st.form_submit_button() triggers a rerun
# Use forms to prevent excessive reruns when collecting multiple inputs

with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hello {name}, you are {age} years old.")
    # This block runs ONLY when the submit button is clicked
```

---

## 14. Deployment & Terminal Commands

| Theme | Function | Explanation / Keywords | Syntax Example |
|-------|----------|------------------------|----------------|
| **Local Run** | `streamlit run` | Run app locally for development | `streamlit run app.py` |
| **Specify Port** | `--server.port` | Run on custom port | `streamlit run app.py --server.port 8502` |
| **Headless** | `--server.headless true` | Run without opening browser | `streamlit run app.py --server.headless true` |
| **Address** | `--server.address` | Bind to specific IP | `streamlit run app.py --server.address 0.0.0.0` |
| **Watchdog** | `--server.fileWatcherType` | Control file watching | `streamlit run app.py --server.fileWatcherType none` |
| **Config File** | `.streamlit/config.toml` | Persistent configuration | `[server]\nport = 8501\nheadless = true` |
| **Secrets** | `.streamlit/secrets.toml` | Store API keys and passwords | `[api]\nkey = "sk-..."` then `st.secrets["api"]["key"]` |
| **Community Cloud** | `share.streamlit.io` | Free cloud deployment | Push to GitHub, connect repo at share.streamlit.io |
| **Docker** | `Dockerfile` | Containerize the app | `FROM python:3.11; RUN pip install streamlit; CMD ["streamlit", "run", "app.py"]` |

### How the App Looks in Terminal vs Browser

**Terminal Screen:**
```bash
$ streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.42:8501

# Logs appear here as users interact with the app
# Errors and stack traces print here
# Press CTRL+C to stop the server
```

**Browser Screen:**
```
+----------------------------------------------------------+
|  Streamlit App Title                          [Rerun] [⋮] |
+----------------------------------------------------------+
|  [Sidebar]  |  Main Content Area                        |
|  Controls   |  - Text elements                          |
|  Filters    |  - Data tables                            |
|  Navigation |  - Charts & visualizations                |
|             |  - Input widgets                          |
|             |                                           |
+----------------------------------------------------------+
|  Status: Running at localhost:8501                       |
+----------------------------------------------------------+
```

**Two-Screen Development Workflow:**
1. **Terminal (Left Screen):** Run `streamlit run app.py` and monitor logs
2. **Browser (Right Screen):** Open `http://localhost:8501` and interact
3. **Edit code** in your editor → Save file → Browser auto-refreshes
4. **Check terminal** for errors → Fix → Save → Repeat

---

## 15. Common Patterns & How to Interpret Results

### Pattern 1: Button Persistence with Session State
```python
if "clicked" not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button("Click me", on_click=click_button)
if st.session_state.clicked:
    st.write("Button was clicked!")  # Persists across reruns
```
**Interpretation:** Without session state, `st.button()` returns `True` only for one rerun. Using `on_click` callback to update session state makes the effect persistent.

### Pattern 2: Conditional Display Based on Selection
```python
option = st.selectbox("Choose analysis", ["Summary", "Detail", "Chart"])
if option == "Summary":
    st.write(df.describe())
elif option == "Detail":
    st.dataframe(df)
else:
    st.bar_chart(df["value"])
```
**Interpretation:** The script reruns top-to-bottom on every widget change. Only the branch matching the current `option` value executes and renders.

### Pattern 3: Expensive Computation with Caching
```python
@st.cache_data
def load_and_process(url):
    df = pd.read_csv(url)
    return df.groupby("category").sum()

result = load_and_process("https://example.com/data.csv")
st.write(result)
```
**Interpretation:** First call computes and caches. Subsequent calls with the same `url` return cached result instantly. Cache clears when function code changes.

### Pattern 4: File Upload and Processing
```python
uploaded = st.file_uploader("Upload CSV", type="csv")
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write(f"Uploaded {len(df)} rows")
    st.dataframe(df.head())
```
**Interpretation:** `uploaded` is `None` initially. After user selects a file, the script reruns and `uploaded` contains a `UploadedFile` object (file-like buffer).

### Pattern 5: Real-time Chat Interface
```python
prompt = st.chat_input("Say something")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"Echo: {prompt}")
```
**Interpretation:** `st.chat_input()` returns the user's message only when submitted. `st.chat_message()` creates styled bubbles. Previous messages persist because the script reruns and rebuilds the entire chat history.

### Pattern 6: Editable Data with Change Tracking
```python
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
edited = st.data_editor(df, key="editor")
st.write("Changes:", st.session_state["editor"])
```
**Interpretation:** `edited` contains the full modified DataFrame. `st.session_state["editor"]` contains only the deltas: `{"edited_rows": {...}, "added_rows": [...], "deleted_rows": [...]}`.

### Pattern 7: Multi-Page App with Dynamic Navigation
```python
import streamlit as st

login = st.Page("login.py", title="Log in")
dashboard = st.Page("dashboard.py", title="Dashboard")
settings = st.Page("settings.py", title="Settings")

if st.session_state.get("logged_in"):
    pg = st.navigation([dashboard, settings])
else:
    pg = st.navigation([login])

pg.run()
```
**Interpretation:** `st.navigation()` returns a page object. Calling `.run()` executes the selected page's script. Pages not in the navigation list are inaccessible.

---

## Quick Reference: Widget Value Types

| Widget | Returns | Default if Empty |
|--------|---------|------------------|
| `st.button()` | `bool` | `False` |
| `st.checkbox()` | `bool` | `False` |
| `st.toggle()` | `bool` | `False` |
| `st.radio()` | Selected option | First option |
| `st.selectbox()` | Selected option | First option |
| `st.multiselect()` | `list` | `[]` |
| `st.slider()` | `int` / `float` / `tuple` | `min_value` |
| `st.select_slider()` | Selected option | First option |
| `st.number_input()` | `int` / `float` | `value` param |
| `st.text_input()` | `str` | `""` |
| `st.text_area()` | `str` | `""` |
| `st.date_input()` | `datetime.date` | `value` param |
| `st.time_input()` | `datetime.time` | `value` param |
| `st.color_picker()` | `str` (hex) | `"#000000"` |
| `st.file_uploader()` | `UploadedFile` or `list` | `None` |
| `st.camera_input()` | `UploadedFile` | `None` |
| `st.chat_input()` | `str` or `None` | `None` |

---

*Generated: 2026-05-11 | Sources: Streamlit Official Docs 1.40+, Streamlit API Reference, Streamlit Community Tutorials*
