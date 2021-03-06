#!/usr/bin/env python3

""" This module can be used to execute json requests to every available LoL API """

import requests

# Default values
api_base_url = "https://{}.api.riotgames.com/lol"
default_region = "euw1"
default_locale = "en_US"


def get_champion_masteries_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/champion-mastery/v3/champion-masteries/by-summoner/{}?api_key={}".format(api_base_url.format(region),
                                                                                       summoner_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_champion_masteries_by_champion_and_summoner_id(champion_id, summoner_id, api_token, region=default_region):
    """
    Input:
        Required: champion_id
                  summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not champion_id or not summoner_id or not api_token:
        return -1

    url = "{}/champion-mastery/v3/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}".format(
        api_base_url.format(region), summoner_id, champion_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_champion_mastery_scores_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/champion-mastery/v3/scores/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id,
                                                                           api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_available_champions(api_token, free_to_play="false", region=default_region):
    """
    Input:
        Required: api_token
        Optional: free_to_play, possibilities: [true, false]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/platform/v3/champions?freeToPlay={}&api_key={}".format(api_base_url.format(region), free_to_play,
                                                                     api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_champion_by_id(champion_id, api_token, region=default_region):
    """
    Input:
        Required: champion_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not champion_id or not api_token:
        return -1

    url = "{}/platform/v3/champions/{}?api_key={}".format(api_base_url.format(region), champion_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_challenger_leagues_by_queue(api_token, queue="RANKED_SOLO_5x5", region=default_region):
    """
    Input:
        Required: api_token
        Optional: queue, possibilities: [RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/league/v3/challengerleagues/by-queue/{}?api_key={}".format(api_base_url.format(region), queue, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_leagues_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/league/v3/leagues/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_master_leagues_by_queue(api_token, queue="RANKED_SOLO_5x5", region=default_region):
    """
    Input:
        Required: api_token
        Optional: queue, possibilities: [RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/league/v3/masterleagues/by-queue/{}?api_key={}".format(api_base_url.format(region), queue, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_positions_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/league/v3/positions/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_champions_info(api_token, locale=default_locale, version="", tags=None, data_by_id="false",
                       region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,       lore
                                        allytips,  partype
                                        blurb,     passive
                                        enemytips, recommended
                                        format,    skins
                                        image,     spells
                                        info,      stats
                                        keys,      tags]
                  data_by_id, possibilities: [true, false]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/champions?locale={}&version={}{}&dataById={}&api_key={}".format(
        api_base_url.format(region), locale, version, format_tags_to_string(tags), data_by_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_champion_info_by_champion_id(champion_id, api_token, locale=default_locale, version="", tags=None,
                                     data_by_id="false", region=default_region):
    """
    Input:
        Required: champion_id
                  api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,       lore
                                        allytips,  partype
                                        blurb,     passive
                                        enemytips, recommended
                                        format,    skins
                                        image,     spells
                                        info,      stats
                                        keys,      tags]
                  data_by_id, possibilities: [true, false]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not champion_id or not api_token:
        return -1

    url = "{}/static-data/v3/champions/{}?locale={}&version={}{}&dataById={}&api_key={}".format(
        api_base_url.format(region), champion_id, locale, version, format_tags_to_string(tags), data_by_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_items_info(api_token, locale=default_locale, version="", tags=None, region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,           inStore
                                        colloq,        into
                                        consumeOnFull, maps
                                        consumed,      requiredChampion
                                        depth,         sanitizedDescription
                                        effect,        specialRecipe
                                        from,          stacks
                                        gold,          stats
                                        groups,        tags
                                        hideFromAll,   tree
                                        image                               ]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/items?locale={}&version={}{}&api_key={}".format(api_base_url.format(region), locale,
                                                                             version, format_tags_to_string(tags),
                                                                             api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_item_info_by_item_id(item_id, api_token, locale=default_locale, version="", tags=None, region=default_region):
    """
    Input:
        Required: item_id
                  api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,           inStore
                                        colloq,        into
                                        consumeOnFull, maps
                                        consumed,      requiredChampion
                                        depth,         sanitizedDescription
                                        effect,        specialRecipe
                                        from,          stacks
                                        gold,          stats
                                        groups,        tags
                                        hideFromAll,   tree
                                        image                               ]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not item_id or not api_token:
        return -1

    url = "{}/static-data/v3/items/{}?locale={}&version={}{}&api_key={}".format(api_base_url.format(region), item_id,
                                                                                locale, version,
                                                                                format_tags_to_string(tags), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_language_strings(api_token, locale=default_locale, version="", region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/language-strings?locale={}&version={}&api_key={}".format(api_base_url.format(region),
                                                                                      locale, version, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_languages(api_token, region=default_region):
    """
    Input:
        Required: api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/languages?api_key={}".format(api_base_url.format(region), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_maps(api_token, locale=default_locale, version="", region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/maps?locale={}&version={}&api_key={}".format(api_base_url.format(region), locale, version,
                                                                          api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_masteries_info(api_token, locale=default_locale, version="", tags=None, region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all, image, masteryTree, prereq, ranks, sanitizedDescription, tree]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/masteries?locale={}&version={}{}&api_key={}".format(api_base_url.format(region), locale,
                                                                                 version, format_tags_to_string(tags),
                                                                                 api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_mastery_info_by_mastery_id(mastery_id, api_token, locale=default_locale, version="", tags=None,
                                   region=default_region):
    """
    Input:
        Required: mastery_id
                  api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all, image, masteryTree, prereq, ranks, sanitizedDescription]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not mastery_id or not api_token:
        return -1

    url = "{}/static-data/v3/masteries/{}?locale={}&version={}{}&api_key={}".format(api_base_url.format(region),
                                                                                    mastery_id, locale, version,
                                                                                    format_tags_to_string(tags),
                                                                                    api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_profile_icons(api_token, locale=default_locale, version="", region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/profile-icons?locale={}&version={}&api_key={}".format(api_base_url.format(region), locale,
                                                                                   version, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_realms(api_token, region=default_region):
    """
    Input:
        Required: api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/realms?api_key={}".format(api_base_url.format(region), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_runes_info(api_token, locale=default_locale, version="", tags=None, region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all, image, sanitizedDescription, stats, tags]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/runes?locale={}&version={}{}&api_key={}".format(api_base_url.format(region), locale,
                                                                             version, format_tags_to_string(tags),
                                                                             api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_rune_info_by_rune_id(rune_id, api_token, locale=default_locale, version="", tags=None, region=default_region):
    """
    Input:
        Required: rune_id
                  api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all, image, sanitizedDescription, stats, tags]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not rune_id or not api_token:
        return -1

    url = "{}/static-data/v3/runes/{}?locale={}&version={}{}&api_key={}".format(api_base_url.format(region), rune_id,
                                                                                locale, version,
                                                                                format_tags_to_string(tags), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_summoner_spells_info(api_token, locale=default_locale, version="", tags=None, data_by_id="false",
                             region=default_region):
    """
    Input:
        Required: api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,          leveltip
                                        cooldown,     maxrank
                                        cooldownBurn, modes
                                        cost,         range
                                        costBurn,     rangeBurn
                                        costType,     resource
                                        effect,       sanitizedDescription
                                        effectBurn,   sanitizedTooltip
                                        image,        tooltip
                                        key,          vars]
                  data_by_id, possibilities: [true, false]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/summoner-spells?locale={}&version={}{}&dataById={}&api_key={}".format(
        api_base_url.format(region), locale, version, format_tags_to_string(tags), data_by_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_summoner_spell_info_by_spell_id(spell_id, api_token, locale=default_locale, version="", tags=None,
                                        data_by_id="false", region=default_region):
    """
    Input:
        Required: spell_id
                  api_token
        Optional: locale, possibilities: [cs_CZ, es_ES, pt_BR
                                          de_DE, es_MX, ro_RO
                                          el_GR, fr_FR, ru_RU
                                          en_AU, hu_HU, th_TH
                                          en_GB, id_ID, tr_TR
                                          en_PH, it_IT, vn_VN
                                          en_PL, ja_JP, zh_CN
                                          en_SG, ko_KR, zh_MY
                                          en_US, ms_MY, zh_TW
                                          es_AR, pl_PL       ]
                  version
                  tags, possibilities: [all,          leveltip
                                        cooldown,     maxrank
                                        cooldownBurn, modes
                                        cost,         range
                                        costBurn,     rangeBurn
                                        costType,     resource
                                        effect,       sanitizedDescription
                                        effectBurn,   sanitizedTooltip
                                        image,        tooltip
                                        key,          vars]
                  data_by_id, possibilities: [true, false]
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not spell_id or not api_token:
        return -1

    url = "{}/static-data/v3/summoner-spells/{}?locale={}&version={}{}&dataById={}&api_key={}".format(
        api_base_url.format(region), spell_id, locale, version, format_tags_to_string(tags), data_by_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_versions(api_token, region=default_region):
    """
    Input:
        Required: api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/static-data/v3/versions?api_key={}".format(api_base_url.format(region), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_shard_data(api_token, region=default_region):
    """
    Input:
        Required: api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/status/v3/shard-data?api_key={}".format(api_base_url.format(region), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_masteries_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/platform/v3/masteries/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id,
                                                                      api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_match_info_by_match_id(match_id, api_token, region=default_region):
    """
    Input:
        Required: match_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not match_id or not api_token:
        return -1

    url = "{}/match/v3/matches/{}?api_key={}".format(api_base_url.format(region), match_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_match_list_by_account_id(account_id, api_token, queue="", end_time="", begin_index="", begin_time="", season="",
                                 champion="", end_index="", region=default_region):
    """
    Input:
        Required: account_id
                  api_token
        Optional: queue
                  endTime
                  beginIndex
                  beginTime
                  season
                  champion
                  endIndex
                  region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not account_id or not api_token:
        return -1

    url = "{}/match/v3/matchlists/by-account/{}?queue={}&endTime&beginIndex={}&beginTime={}&season={}&champion={}&endIndex={}&api_key={}".format(
        api_base_url.format(region), account_id, queue, end_time, begin_index, begin_time, season, champion, end_index,
        api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_recent_match_list_by_account_id(account_id, api_token, region=default_region):
    """
    Input:
        Required: account_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not account_id or not api_token:
        return -1

    url = "{}/match/v3/matchlists/by-account/{}/recent?api_key={}".format(api_base_url.format(region), account_id,
                                                                          api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_timeline_by_match_id(match_id, api_token, region=default_region):
    """
    Input:
        Required: match_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not match_id or not api_token:
        return -1

    url = "{}/match/v3/timelines/by-match/{}?api_key={}".format(api_base_url.format(region), match_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_runes_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/platform/v3/runes/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_active_game_info_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/spectator/v3/active-games/by-summoner/{}?api_key={}".format(api_base_url.format(region), summoner_id,
                                                                          api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_featured_games(api_token, region=default_region):
    """
    Input:
        Required: api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not api_token:
        return -1

    url = "{}/spectator/v3/featured-games?api_key={}".format(api_base_url.format(region), api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_summoner_info_by_account_id(account_id, api_token, region=default_region):
    """
    Input:
        Required: account_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not account_id or not api_token:
        return -1

    url = "{}/summoner/v3/summoners/by-account/{}?api_key={}".format(api_base_url.format(region), account_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_summoner_info_by_summoner_name(summoner_name, api_token, region=default_region):
    """
    Input:
        Required: summoner_name
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_name or not api_token:
        return -1

    url = "{}/summoner/v3/summoners/by-name/{}?api_key={}".format(api_base_url.format(region), summoner_name, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def get_summoner_info_by_summoner_id(summoner_id, api_token, region=default_region):
    """
    Input:
        Required: summoner_id
                  api_token
        Optional: region, possibilities: [RU, KR, BR1, OC1, JP1, NA1, EUN1, EUW1, TR1, LA1, LA2]
    Output:
        Success: JSON response object
        Failure: -1, one or more required arguments are missing
    """
    if not summoner_id or not api_token:
        return -1

    url = "{}/summoner/v3/summoners/{}?api_key={}".format(api_base_url.format(region), summoner_id, api_token)
    response = requests.get(url)
    data = response.json()
    return data


def format_tags_to_string(tags):
    """
    Input: tags
    Output: formatted url string
    """
    formatted_url_string = ""
    if tags:
        for tag in tags:
            formatted_url_string += "&tags={}".format(tag)
    return formatted_url_string
