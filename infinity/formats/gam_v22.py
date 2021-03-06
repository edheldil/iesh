# -*-python-*-
# ie_shell.py - Simple shell for Infinity Engine-based game files
# Copyright (C) 2004-2009 by Jaroslav Benkovsky, <edheldil@users.sf.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# Conforms to IESDP 18.10.2019

from infinity.format import Format, register_format


class GAM_V22_Format (Format):

    header_desc = (
            { 'key': 'signature',
              'type': 'STR4',
              'off': 0x0000,
              'label': 'Signature',
              'default': 'GAME' },

            { 'key': 'version',
              'type': 'STR4',
              'off': 0x0004,
              'label': 'Version',
              'default': 'V2.2'},

            { 'key': 'game_time',
              'type': 'DWORD',
              'off': 0x0008,
              'label': 'Game time (300 units==1 hour)' },

            { 'key': 'formation',
              'type': 'WORD',
              'off': 0x000C,
              'label': 'Selected formation'},

            { 'key': 'formation_button',
              'type': 'WORD',
              'off': 0x000E,
              'count': 5,
              'label': 'Formation button'},

            { 'key': 'gold',
              'type': 'DWORD',
              'off': 0x0018,
              'label': 'Party gold'},

            { 'key': 'pc_cnt0',
              'type': 'WORD',
              'off': 0x001C,
              'label': 'Unknown / PC count'},

            { 'key': 'weather',
              'type': 'WORD',
              'off': 0x001E,
              'mask': { 0x01: 'rain', 0x02: 'snow' },
              'label': 'Weather'},

            { 'key': 'pc_off',
              'type': 'DWORD',
              'off': 0x0020,
              'label': 'PC offset'},

            { 'key': 'pc_cnt',
              'type': 'DWORD',
              'off': 0x0024,
              'label': 'PC count (incl. protagonist)'},

            { 'key': 'unknown28',
              'type': 'DWORD',
              'off': 0x0028,
              'label': '(offset to party inventory)'},

            { 'key': 'unknown2C',
              'type': 'DWORD',
              'off': 0x002C,
              'label': '(count of party inventory)'},

            { 'key': 'npc_off',
              'type': 'DWORD',
              'off': 0x0030,
              'label': 'NPC offset'},

            { 'key': 'npc_cnt',
              'type': 'DWORD',
              'off': 0x0034,
              'label': 'NPC count'},

            { 'key': 'global_off',
              'type': 'DWORD',
              'off': 0x0038,
              'label': 'GLOBAL variables offset'},

            { 'key': 'global_cnt',
              'type': 'DWORD',
              'off': 0x003C,
              'label': 'GLOBAL variables count'},

            { 'key': 'main_area',
              'type': 'RESREF',
              'off': 0x0040,
              'label': 'Main area'},

            { 'key': 'familiar_extra_off',
              'type': 'DWORD',
              'off': 0x0048,
              'label': 'Unknown / Familiar extra offset'},

            { 'key': 'journal_entry_cnt',
              'type': 'DWORD',
              'off': 0x004C,
              'label': 'Journal entries count'},

            { 'key': 'journal_entry_off',
              'type': 'DWORD',
              'off': 0x0050,
              'label': 'Journal entries offset'},

            { 'key': 'reputation',
              'type': 'DWORD',
              'off': 0x0054,
              'label': 'Party reputation (*10)'},

            { 'key': 'current_area',
              'type': 'RESREF',
              'off': 0x0058,
              'label': 'Current area'},

            { 'key': 'gui_flags',
              'type': 'DWORD',
              'off': 0x0060,
              'mask': {0x01: 'party_ai_enabled',
                       0x02: 'text_window_size1',
                       0x04: 'text_window_size2',
                       0x08: 'unknown bit3',
                       0x10: 'hide_gui',
                       0x20: 'hide_options',
                       0x40: 'hide_portraits',
                       0x80: 'hide_automap_notes' },
              'label': 'GUI flags'},

            { 'key': 'loading_progress',
              'type': 'DWORD',
              'off': 0x0064,
              'enum': {0: 'restrict_xp_to_bg1_limit',
                       1: 'restrict_xp_to_totsc_limit',
                       2: 'restrict_xp_to_soa_limit',
                       3: 'XNEWAREA.2DA processing to be done',
                       4: 'XNEWAREA.2DA processing complete',
                       5: 'TOB active'},
              'label': 'Unknown / Loading progress'},

            { 'key': 'familiar_off',
              'type': 'DWORD',
              'off': 0x0068,
              'label': 'Familiar info offset'},

            { 'key': 'stored_location_off',
              'type': 'DWORD',
              'off': 0x006C,
              'label': 'Stored locations offset'},

            { 'key': 'stored_location_cnt',
              'type': 'DWORD',
              'off': 0x0070,
              'label': 'Stored locations count'},

            { 'key': 'game_time',
              'type': 'DWORD',
              'off': 0x0074,
              'label': 'Game time (real seconds)'},

            { 'key': 'pocket_plane_location_off',
              'type': 'DWORD',
              'off': 0x0078,
              'label': 'Pocket plane locations offset'},

            { 'key': 'pocket_plane_location_cnt',
              'type': 'DWORD',
              'off': 0x007C,
              'label': 'Pocket plane locations count'},

            { 'key': 'unknown80',
              'type': 'BYTES',
              'off': 0x0080,
              'size': 52,
              'label': 'Unknown 80'},
    )

    npc_desc = (
            { 'key': 'character_selection',
              'type': 'WORD',
              'off': 0x0000,
              'enum': {0: 'not selected', 1: 'selected', 0x8000: 'dead'},
              'label': 'Character selection'},

            { 'key': 'party_order',
              'type': 'WORD',
              'off': 0x0002,
              'label': 'Party order'},

            { 'key': 'cre_off',
              'type': 'DWORD',
              'off': 0x0004,
              'label': 'CRE offset'},

            { 'key': 'cre_size',
              'type': 'DWORD',
              'off': 0x0008,
              'label': 'CRE size'},

            { 'key': 'character_name',
              'type': 'STR8',
              'off': 0x000C,
              'size': 8,
              'label': 'Character name'},

            { 'key': 'orientation',
              'type': 'DWORD',
              'off': 0x0014,
              'label': 'Orientation'},

            { 'key': 'current_area',
              'type': 'RESREF',
              'off': 0x0018,
              'label': 'Current area'},

            { 'key': 'x',
              'type': 'WORD',
              'off': 0x0020,
              'label': 'X coordinate'},

            { 'key': 'y',
              'type': 'WORD',
              'off': 0x0022,
              'label': 'Y coordinate'},

            { 'key': 'view_x',
              'type': 'WORD',
              'off': 0x0024,
              'label': 'Viewing rectange X coordinate'},

            { 'key': 'view_y',
              'type': 'WORD',
              'off': 0x0026,
              'label': 'Viewing rectangle Y coordinate'},

            { 'key': 'modal_action',
              'type': 'WORD',
              'off': 0x0028,
              'label': 'Modal action'},

            { 'key': 'happiness',
              'type': 'WORD',
              'off': 0x002A,
              'label': 'Happiness'},

            { 'key': 'num_times_interacted_npc_count',
              'type': 'DWORD',
              'off': 0x002C,
              'count': 24,
              'label': 'Num times interacted NPC count (unused)' },

            { 'key': 'quick_weapon_slot_index',
              'type': 'WORD',
              'off': 0x008C,
              'count': 8,
              'label': 'Index into slots.ids for main Quick Weapon or offhand, interchanging (FFFF=none)' },

            { 'key': 'quick_slot_usable',
              'type': 'WORD',
              'off': 0x009C,
              'count': 8,
              'label': 'Is the quick weapon slot usable?' },

            { 'key': 'quick_spell_resource',
              'type': 'RESREF',
              'off': 0x00AC,
              'count': 9,
              'label': 'Quick spell resource' },

            { 'key': 'quick_spell_class',
              'type': 'BYTE',
              'off': 0x00F4,
              'count': 9,
              'label': 'Quick spell class' },

            { 'key': 'quick_spell_unknown',
              'type': 'BYTE',
              'off': 0x00FD,
              'count': 1,
              'label': '(Quick spell) unknown' },

            { 'key': 'quick_item_slot_index',
              'type': 'WORD',
              'off': 0x00FE,
              'count': 3,
              'label': 'Index into slots.ids for Quick Item (FFFF=none)' },

            { 'key': 'quick_item_slot_ability',
              'type': 'WORD',
              'off': 0x0104,
              'count': 3,
              'label': 'Quick Item slot usable' },

            { 'key': 'quick_innate',
              'type': 'RESREF',
              'off': 0x010A,
              'count': 9,
              'label': 'Quick innate' },

            { 'key': 'quick_song',
              'type': 'RESREF',
              'off': 0x0152,
              'count': 9,
              'label': 'Quick song' },

            { 'key': 'quick_slot',
              'type': 'RESREF',
              'off': 0x019A,
              'count': 9,
              'label': 'Quick slot' },

            { 'key': 'name',
              'type': 'STR32',
              'off': 0x01BE,
              'label': 'Name' },

            { 'key': 'talkcount',
              'type': 'DWORD',
              'off': 0x01C2,
              'label': 'Talkcount' },

            { 'key': 'stats',
              'type': 'BYTES',
              'off': 0x01C6,
              'size': 116,
              'label': 'Stats' },

            { 'key': 'soundset',
              'type': 'RESREF',
              'off': 0x023A,
              'label': 'Sound set' },

            { 'key': 'voiceset',
              'type': 'STR32',
              'off': 0x0242,
              'label': 'Voice set' },

            { 'key': 'unknown_1',
              'type': 'DWORD',
              'off': 0x0262,
              'label': 'Unknown 1' },

            { 'key': 'unknown_2',
              'type': 'DWORD',
              'off': 0x0266,
              'label': 'Unknown 2' },

            { 'key': 'unknown_3',
              'type': 'DWORD',
              'off': 0x026A,
              'label': 'Unknown 3' },

            { 'key': 'expertise',
              'type': 'DWORD',
              'off': 0x026E,
              'label': 'Expertise' },

            { 'key': 'power_attack',
              'type': 'DWORD',
              'off': 0x0272,
              'label': 'Power attack' },

            { 'key': 'arterial_strike',
              'type': 'DWORD',
              'off': 0x0276,
              'label': 'Arterial Strike' },

            { 'key': 'hamstring',
              'type': 'DWORD',
              'off': 0x027A,
              'label': 'Hamstring' },

            { 'key': 'rapid_shot',
              'type': 'DWORD',
              'off': 0x027E,
              'label': 'Rapid Shot' },

            { 'key': 'unknown_4',
              'type': 'DWORD',
              'off': 0x0282,
              'label': 'Unknown 4' },

            { 'key': 'unknown_5',
              'type': 'BYTES',
              'size': 3,
              'off': 0x0286,
              'label': 'Unknown 5' },

            { 'key': 'selected_w_slot',
              'type': 'WORD',
              'off': 0x0289,
              'label': 'Selected weapon slot' },

            { 'key': 'unknown_6',
              'type': 'BYTES',
              'size': 153,
              'off': 0x028B,
              'label': 'Unknown 6' },

    )

    pc_desc = npc_desc

    global_desc = (
            { 'key': 'name',
              'type': 'STR32',
              'off': 0x0000,
              'label': 'Variable name' },

            { 'key': 'type',
              'type': 'WORD',
              'off': 0x0020,
              # TODO: add mask:  (bit 0: int, bit 1: float, bit 2: script name, bit 3: resref, bit 4: strref, bit 5: dword)
              'label': 'Type' },

            { 'key': 'refval',
              'type': 'WORD',
              'off': 0x0022,
              'label': 'Ref value' },

            { 'key': 'dwval',
              'type': 'DWORD',
              'off': 0x0024,
              'label': 'DWORD value' },

            { 'key': 'intval',
              'type': 'DWORD',
              'off': 0x0028,
              'label': 'INT value' },

            { 'key': 'dblval',
              'type': 'BYTES',
              'off': 0x002c,
              'size': 8,
              'label': 'DOUBLE value' },

            { 'key': 'scrnameval',
              'type': 'BYTES',
              'off': 0x0033,
              'size': 32,
              'label': 'Script name value' },
    )

    journal_entry_desc = (
            { 'key': 'text',
              'type': 'STRREF',
              'off': 0x0000,
              'label': 'Journal text' },

            { 'key': 'time',
              'type': 'DWORD',
              'off': 0x0004,
              'label': 'Time (secs)' },

            { 'key': 'current_chapter',
              'type': 'BYTE',
              'off': 0x0008,
              'label': 'Current chapter number' },

            { 'key': 'unknown09',
              'type': 'BYTE',
              'off': 0x0009,
              'label': 'Unknown 09' },

            { 'key': 'section',
              'type': 'BYTE',
              'off': 0x000A,
              'mask': { 0x01: 'quests', 0x02: 'Completed quests', 0x04: 'Journal info' },
              'label': 'Journal section' },

            { 'key': 'location_flag',
              'type': 'BYTE',
              'off': 0x000B,
              'enum': { 0x1F: 'external TOT/TOH', 0xFF: 'internal TLK' },
              'label': 'Location flag' },
    )

    familiar_info_desc = (
            { 'key': 'lg_familiar',
              'type': 'RESREF',
              'off': 0x0000,
              'label': 'Lawful  familiar' },

            { 'key': 'ln_familiar',
              'type': 'RESREF',
              'off': 0x0008,
              'label': 'Lawful neutral familiar' },

            { 'key': 'le_familiar',
              'type': 'RESREF',
              'off': 0x0010,
              'label': 'Lawful evil familiar' },


            { 'key': 'ng_familiar',
              'type': 'RESREF',
              'off': 0x0018,
              'label': 'Neutral good familiar' },

            { 'key': 'nn_familiar',
              'type': 'RESREF',
              'off': 0x0020,
              'label': 'True neutral familiar' },

            { 'key': 'ne_familiar',
              'type': 'RESREF',
              'off': 0x0028,
              'label': 'Neutral evil familiar' },


            { 'key': 'cg_familiar',
              'type': 'RESREF',
              'off': 0x0030,
              'label': 'Chaotic  familiar' },

            { 'key': 'cn_familiar',
              'type': 'RESREF',
              'off': 0x0038,
              'label': 'Chaotic neutral familiar' },

            { 'key': 'ce_familiar',
              'type': 'RESREF',
              'off': 0x0040,
              'label': 'Chaotic evil familiar' },

            { 'key': 'unknown48',
              'type': 'DWORD',
              'off': 0x0048,
              'label': 'Unknown 48' },


            { 'key': 'lg_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x004C,
              'label': 'LG level 1 familiar count' },

            { 'key': 'lg_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0050,
              'label': 'LG level 2 familiar count' },

            { 'key': 'lg_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0054,
              'label': 'LG level 3 familiar count' },

            { 'key': 'lg_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0058,
              'label': 'LG level 4 familiar count' },

            { 'key': 'lg_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x005C,
              'label': 'LG level 5 familiar count' },

            { 'key': 'lg_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0060,
              'label': 'LG level 6 familiar count' },

            { 'key': 'lg_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0064,
              'label': 'LG level 7 familiar count' },

            { 'key': 'lg_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0068,
              'label': 'LG level 8 familiar count' },

            { 'key': 'lg_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x006C,
              'label': 'LG level 9 familiar count' },


            { 'key': 'ln_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0070,
              'label': 'LN level 1 familiar count' },

            { 'key': 'ln_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0074,
              'label': 'LN level 2 familiar count' },

            { 'key': 'ln_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0078,
              'label': 'LN level 3 familiar count' },

            { 'key': 'ln_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x007C,
              'label': 'LN level 4 familiar count' },

            { 'key': 'ln_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0080,
              'label': 'LN level 5 familiar count' },

            { 'key': 'ln_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0084,
              'label': 'LN level 6 familiar count' },

            { 'key': 'ln_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0088,
              'label': 'LN level 7 familiar count' },

            { 'key': 'ln_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x008C,
              'label': 'LN level 8 familiar count' },

            { 'key': 'ln_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0090,
              'label': 'LN level 9 familiar count' },


            { 'key': 'cg_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0094,
              'label': 'CG level 1 familiar count' },

            { 'key': 'cg_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0098,
              'label': 'CG level 2 familiar count' },

            { 'key': 'cg_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x009C,
              'label': 'CG level 3 familiar count' },

            { 'key': 'cg_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00A0,
              'label': 'CG level 4 familiar count' },

            { 'key': 'cg_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00A4,
              'label': 'CG level 5 familiar count' },

            { 'key': 'cg_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00A8,
              'label': 'CG level 6 familiar count' },

            { 'key': 'cg_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00AC,
              'label': 'CG level 7 familiar count' },

            { 'key': 'cg_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00B0,
              'label': 'CG level 8 familiar count' },

            { 'key': 'cg_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00B4,
              'label': 'CG level 9 familiar count' },


            { 'key': 'ng_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00B8,
              'label': 'NG level 1 familiar count' },

            { 'key': 'ng_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00BC,
              'label': 'NG level 2 familiar count' },

            { 'key': 'ng_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00C0,
              'label': 'NG level 3 familiar count' },

            { 'key': 'ng_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00C4,
              'label': 'NG level 4 familiar count' },

            { 'key': 'ng_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00C8,
              'label': 'NG level 5 familiar count' },

            { 'key': 'ng_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00CC,
              'label': 'NG level 6 familiar count' },

            { 'key': 'ng_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00D0,
              'label': 'NG level 7 familiar count' },

            { 'key': 'ng_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00D4,
              'label': 'NG level 8 familiar count' },

            { 'key': 'ng_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00D8,
              'label': 'NG level 9 familiar count' },


            { 'key': 'tn_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00DC,
              'label': 'TN level 1 familiar count' },

            { 'key': 'tn_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00E0,
              'label': 'TN level 2 familiar count' },

            { 'key': 'tn_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00E4,
              'label': 'TN level 3 familiar count' },

            { 'key': 'tn_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00E8,
              'label': 'TN level 4 familiar count' },

            { 'key': 'tn_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00EC,
              'label': 'TN level 5 familiar count' },

            { 'key': 'tn_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00F0,
              'label': 'TN level 6 familiar count' },

            { 'key': 'tn_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00F4,
              'label': 'TN level 7 familiar count' },

            { 'key': 'tn_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00F8,
              'label': 'TN level 8 familiar count' },

            { 'key': 'tn_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x00FC,
              'label': 'TN level 9 familiar count' },


            { 'key': 'ne_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0100,
              'label': 'NE level 1 familiar count' },

            { 'key': 'ne_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0104,
              'label': 'NE level 2 familiar count' },

            { 'key': 'ne_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0108,
              'label': 'NE level 3 familiar count' },

            { 'key': 'ne_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x010C,
              'label': 'NE level 4 familiar count' },

            { 'key': 'ne_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0110,
              'label': 'NE level 5 familiar count' },

            { 'key': 'ne_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0114,
              'label': 'NE level 6 familiar count' },

            { 'key': 'ne_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0118,
              'label': 'NE level 7 familiar count' },

            { 'key': 'ne_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x011C,
              'label': 'NE level 8 familiar count' },

            { 'key': 'ne_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0120,
              'label': 'NE level 9 familiar count' },


            { 'key': 'le_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0124,
              'label': 'LE level 1 familiar count' },

            { 'key': 'le_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0128,
              'label': 'LE level 2 familiar count' },

            { 'key': 'le_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x012C,
              'label': 'LE level 3 familiar count' },

            { 'key': 'le_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0130,
              'label': 'LE level 4 familiar count' },

            { 'key': 'le_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0134,
              'label': 'LE level 5 familiar count' },

            { 'key': 'le_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0138,
              'label': 'LE level 6 familiar count' },

            { 'key': 'le_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x013C,
              'label': 'LE level 7 familiar count' },

            { 'key': 'le_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0140,
              'label': 'LE level 8 familiar count' },

            { 'key': 'le_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0144,
              'label': 'LE level 9 familiar count' },


            { 'key': 'cn_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0148,
              'label': 'CN level 1 familiar count' },

            { 'key': 'cn_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x014C,
              'label': 'CN level 2 familiar count' },

            { 'key': 'cn_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0150,
              'label': 'CN level 3 familiar count' },

            { 'key': 'cn_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0154,
              'label': 'CN level 4 familiar count' },

            { 'key': 'cn_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0158,
              'label': 'CN level 5 familiar count' },

            { 'key': 'cn_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x015C,
              'label': 'CN level 6 familiar count' },

            { 'key': 'cn_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0160,
              'label': 'CN level 7 familiar count' },

            { 'key': 'cn_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0164,
              'label': 'CN level 8 familiar count' },

            { 'key': 'cn_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0168,
              'label': 'CN level 9 familiar count' },


            { 'key': 'ce_1_familiar_cnt',
              'type': 'DWORD',
              'off': 0x016C,
              'label': 'CE level 1 familiar count' },

            { 'key': 'ce_2_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0170,
              'label': 'CE level 2 familiar count' },

            { 'key': 'ce_3_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0174,
              'label': 'CE level 3 familiar count' },

            { 'key': 'ce_4_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0178,
              'label': 'CE level 4 familiar count' },

            { 'key': 'ce_5_familiar_cnt',
              'type': 'DWORD',
              'off': 0x017C,
              'label': 'CE level 5 familiar count' },

            { 'key': 'ce_6_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0180,
              'label': 'CE level 6 familiar count' },

            { 'key': 'ce_7_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0184,
              'label': 'CE level 7 familiar count' },

            { 'key': 'ce_8_familiar_cnt',
              'type': 'DWORD',
              'off': 0x0188,
              'label': 'CE level 8 familiar count' },

            { 'key': 'ce_9_familiar_cnt',
              'type': 'DWORD',
              'off': 0x018C,
              'label': 'CE level 9 familiar count' },
    )

    stored_location_desc = (
            { 'key': 'area',
              'type': 'RESREF',
              'off': 0x0000,
              'label': 'Area' },

            { 'key': 'x',
              'type': 'WORD',
              'off': 0x0008,
              'label': 'X coordinate' },

            { 'key': 'y',
              'type': 'WORD',
              'off': 0x000A,
              'label': 'Y coordinate' },
    )

    pocket_plane_location_desc = stored_location_desc

    def __init__ (self):
        Format.__init__ (self)
        self.expect_signature = 'GAME'
        self.pc_list = []
        self.npc_list = []
        self.global_list = []
        self.journal_entry_list = []
        self.stored_location_list = []
        self.pocket_plane_location_list = []


    def read (self, stream):
        self.read_header (stream)

        self.read_list (stream, 'pc')
        self.read_list (stream, 'npc')
        self.read_list (stream, 'global')
        self.read_list (stream, 'journal_entry')
        self.read_list (stream, 'stored_location')
        self.read_list (stream, 'pocket_plane_location')

        obj = {}
        self.read_struc (stream, self.header['familiar_off'], self.familiar_info_desc, obj)
        self.familiar_info = obj
        # FIXME: familiar info


    def update (self):
        off = self.size_struc (self.header_desc)
        self.header['pc_cnt'] = len (self.pc_list)
        self.header['pc_off'] = off
        off += self.size_struc (self.pc_desc) * len (self.pc_list)

        pass


    def write (self, stream):
        self.write_header (stream)

        off = self.write_list (stream, off, 'actor')
        raise RuntimeError ("Not implemented")


    def printme (self):
        self.print_header ()

        self.print_list ('pc')
        self.print_list ('npc')
        self.print_list ('global')
        self.print_list ('journal_entry')
        self.print_list ('stored_location')
        self.print_list ('pocket_plane_location')

        self.print_struc (self.familiar_info, self.familiar_info_desc)


register_format (GAM_V22_Format, signature='GAMEV2.2', extension='GAM', name=('GAM', 'GAME'), type=0x3f5)
