# Volatility
#
# Authors:
# Mariano `emdel` Graziano - graziano@eurecom.fr
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details. 
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA 
#



revision_id_db = {
    0x0d : "PENRYN",
    0x10 : "SANDY",
    0x0f : "WESTMERE"
}

microarch_db = {
    "penryn" : 0x0d,
    "sandy" : 0x10,
    "westmere" : 0x0f
}

nested_revision_id_db = {
    0x11e57ed0 : "KVM",
    0x01       : "VMware",
    0x40000001 : "Xen"
}
