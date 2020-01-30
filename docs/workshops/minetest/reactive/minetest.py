from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import status_set
import charms.apt

@when_not('apt.installed.minetest')
def install_minetest_apt():
    # charms.apt.queue_install(['python'])
    # export DEBIAN_FRONTEND=noninteractive
    charms.apt.queue_install(['minetest'])
    #sets the 'apt.installed.wordpress' flag when done

@when('apt.installed.minetest')
@when_not('minetest.ready')
def install_minetest():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    status_set('blocked', "minetest installed, waiting for database")
    set_flag('minetest.ready')

@when_not('minetest.ready')
@when_not('apt.installed.minetest')
def waiting_for_minetest():
    status_set('maintenance', "waiting for apt minetest installation")


    