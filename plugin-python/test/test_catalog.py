import logging

from pyvcloud.vcd.client import BasicLoginCredentials
from pyvcloud.vcd.client import Client
from pyvcloud.vcd.client import TaskStatus
from pyvcloud.vcd.org import Org
from pyvcloud.vcd.vapp import VApp
from pyvcloud.vcd.vdc import VDC
#from errors import VappVmCreationError
from pyvcloud.vcd.vm import VM


def vcd_login(host, user, password, org):
    logging.basicConfig(level=logging.DEBUG)
    logging.info("login called")
    client = Client(
        host,
        api_version="27.0",
        verify_ssl_certs=False,
        log_file='vcd.log',
        log_requests=True,
        log_headers=True,
        log_bodies=True)
    try:
        client.set_credentials(BasicLoginCredentials(user, org, password))

        return client
    except Exception as e:
        print('error occured', e)


def update(client, old_name, new_name, description, shared):
    logging.info("__INIT_update_catalog__")
    logging.debug(
        "old_name = [%s] new_name = [%s]  desc = [%s] shared = [%s] ",
        old_name, new_name, description, shared)
    updated = False

    try:
        logged_in_org = client.get_org()
        org = Org(client, resource=logged_in_org)
        try:
            catalog = org.update_catalog(
                old_catalog_name=old_name,
                new_catalog_name=new_name,
                description=description)
            updated = True

            success = share_catalog(client, name, shared)
            if not success:
                updated = False
        except Exception as e:
            logging.info(
                "===_INIT_update old_name = [%s] new_name = [%s]  desc = [%s] shared = [%s] ",
                old_name, new_name, description, shared)
    except Exception as e:
        logging.warn("Error occured while updating catalog ", e)

    logging.debug("__DONE_update_catalog__")
    return updated


def share_catalog(client, name, shared):
    logging.info("__INIT_update_shared_catalog__")
    success = False
    try:
        logged_in_org = client.get_org()
        org = Org(client, resource=logged_in_org)
        try:
            catalog = org.share_catalog(name=name, share=shared)
            success = True
        except Exception as e:
            logging.error(
                "Error occured while updating share_catalog to shared = [%v], __ERROR_MESSAGE__ ",
                shared, str(e))
    except Exception as e:
        logging.error(
            "Error occured while updating share_catalog to shared = [%v], __ERROR_MESSAGE__ ",
            shared, str(e))

    logging.info("__DONE_update_share_catalog__")
    return success


if __name__ == '__main__':
    client = vcd_login("10.172.158.127", "acmeadmin", "VMware1!", "acme")
    #share_catalog(client, "pcp_catalog_01", True)
    update(client, "1", "pcp_catalog_01_updated_02", "desc updated", True)
