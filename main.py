from st_pages import Page, show_pages, add_page_title, Section

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("firstPage.py", "Home", "🏠"),
        Page('other_pages/other.py', "MATH", ":books:"),
        #Section(name="Section test", icon="🎈️"),
        # Pages after a section will be indented
        Page(path="other_pages/page2.py",name='Other', icon="💪"),
        # Unless you explicitly say in_section=False
        #Page("Not in a section", in_section=False)
    ]
    
)
