from . import __version__ as app_version

app_name = "bhumi_awards_portal"
app_title = "Bhumi Awards Portal"
app_publisher = "Hussain"
app_description = "Portal Website for Bhumi NGO."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "t4c@bhumi.ngo"
app_license = "MIT"


# Fixtures 
fixtures = [
    "Color",
    {"dt": "Website Theme", "filters": {"name": "Bhumi Theme"}},
    "Website Settings",
    {"dt": "Role", "filters": {"name": "Voter"}}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bhumi_awards_portal/css/bhumi_awards_portal.css"
# app_include_js = "/assets/bhumi_awards_portal/js/bhumi_awards_portal.js"

# include js, css files in header of web template
# web_include_css = "/assets/bhumi_awards_portal/css/bhumi_awards_portal.css"
# web_include_js = "/assets/bhumi_awards_portal/js/bhumi_awards_portal.js"

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "bhumi_awards_portal/public/scss/website"

brand_html = '<div><img src="/assets/bhumi_logo.png"></div>'
# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "bhumi_awards_portal.utils.jinja_methods",
# 	"filters": "bhumi_awards_portal.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "bhumi_awards_portal.install.before_install"
# after_install = "bhumi_awards_portal.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bhumi_awards_portal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bhumi_awards_portal.tasks.all"
# 	],
# 	"daily": [
# 		"bhumi_awards_portal.tasks.daily"
# 	],
# 	"hourly": [
# 		"bhumi_awards_portal.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bhumi_awards_portal.tasks.weekly"
# 	],
# 	"monthly": [
# 		"bhumi_awards_portal.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "bhumi_awards_portal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bhumi_awards_portal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "bhumi_awards_portal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"bhumi_awards_portal.auth.validate"
# ]

