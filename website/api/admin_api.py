import json
from flask import Blueprint
from website.helpers.require_role import require_role_system_name_on_current_user
from website.logs import get_app_logs
from website.models.suggestion import Suggestion
from website.models.role import Role
from website.models.user import User

admin_api = Blueprint("admin_api", __name__)


@admin_api.route("/app_logs")
@require_role_system_name_on_current_user("editing_app_logs")
def app_logs():
    return json.dumps(get_app_logs())

@admin_api.route("/suggestions")
@require_role_system_name_on_current_user("editing_suggestions")
def suggestions():
    return json.dumps([s.info_for_admin() for s in Suggestion.get_all()])

@admin_api.route("/info_pro_upravu_roli")
@require_role_system_name_on_current_user("editing_roles")
def info_pro_upravu_roli():
    return json.dumps([r.get_info_for_admin() for r in Role.get_all()])

@admin_api.route("/uzivatele_pro_udeleni_roli")
@require_role_system_name_on_current_user("editing_admins")
def uzivatele_pro_udeleni_roli():
    return json.dumps(User.get_seznam_pro_jmenovani_adminu())

@admin_api.route("/role_uzivatele/<int:id>")
@require_role_system_name_on_current_user("editing_admins")
def role_uzivatele(id):
    return json.dumps([r.system_name for r in User.get_by_id(id).roles])

@admin_api.route("/both_names_of_all_roles")
@require_role_system_name_on_current_user("editing_admins")
def both_names_of_all_roles():
    return json.dumps([r.get_info_for_jmenovani() for r in Role.get_all()])

@admin_api.route("/non_admin_users_from_db")
@require_role_system_name_on_current_user("editing_users")
def nonadmin_users():
    return json.dumps([u.get_info_pro_seznam_useru() for u in User.get_all() if "admin" not in [r.system_name for r in u.roles]])

@admin_api.route("/admin_users_from_db")
@require_role_system_name_on_current_user("editing_users")
def admin_users():
    return json.dumps([u.get_info_pro_seznam_useru() for u in User.get_all() if "admin" in [r.system_name for r in u.roles]])

@admin_api.route("/detail_usera/<int:id>")
@require_role_system_name_on_current_user("editing_users")
def detail_usera(id):
    return json.dumps(User.get_by_id(id).get_info_for_admin_detail_usera())

@admin_api.route("/uprava_jazyku")
@require_role_system_name_on_current_user("editing_languages")
def uprava_jazyku():
    return json.dumps([l.get_detail_for_seznam_jazyku() for l in Language.get_all()])

@admin_api.route("/detail_jazyka/<int:id>")
@require_role_system_name_on_current_user("editing_languages")
def detail_jazyka(id):
    return Language.get_by_id(id).get_detail_jazyka()
