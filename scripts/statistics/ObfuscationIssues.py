from scripts.statistics.InterRulesIssue import InterRulesIssue


class ObfuscateIssues:

    ############################################################################################
    ############################################################################################

    dns_crude_rules = set()

    dns_chameleon_rules = set()

    dns_stutter_rules = set()

    dns_duplicate_rules = set()

    dns_overlapping_rules = set()

    dns_orthogonal_rules = set()

    ############################################################################################
    ############################################################################################


    ftp_crude_rules = {
        # ftp_community
        # ftp_ftp
        "1:14770:11",
    }

    ftp_chameleon_rules = set()

    ftp_stutter_rules = {
        # ftp_community
        # ftp_ftp
        "1:13925:12", "1:16357:7", "1:34225:5", "1:45461:2",
    }

    ftp_duplicate_rules = set()

    ftp_overlapping_rules = {
        # ftp_community
        InterRulesIssue('1:1672:22', '1:336:17'), InterRulesIssue('1:1777:19', '1:1778:18'),
        InterRulesIssue('1:1971:13', '1:361:22'), InterRulesIssue('1:2178:23', '1:553:13'),
        # ftp_ftp
        InterRulesIssue('1:16698:4', '1:489:19'), InterRulesIssue('1:1672:22', '1:336:17'),
        InterRulesIssue('1:1777:19', '1:1778:18'), InterRulesIssue('1:1971:13', '1:361:22'),
        InterRulesIssue('1:2179:16', '1:489:19'),
    }

    ftp_orthogonal_rules = {
        # ftp_community
        InterRulesIssue('1:1377:24', '1:2343:14'), InterRulesIssue('1:2332:10', '1:554:10'),
        # ftp_ftp
        InterRulesIssue('1:14770:11', '1:16357:7'), InterRulesIssue('1:14770:11', '1:16524:10'),
        InterRulesIssue('1:14770:11', '1:2343:14'), InterRulesIssue('1:14770:11', '1:34225:5'),
    }

    ############################################################################################
    ############################################################################################


    sip_crude_rules = {
        # sip_voip
        "1:19364:5", "1:19365:5", "1:51504:4", "1:51508:4", "1:51509:4", "1:51760:4", "1:51761:4", "1:51767:4", "1:51772:2",
    }

    sip_chameleon_rules = {
        # sip_voip
        "1:11976:9", "1:11977:9", "1:11979:7", "1:11980:9", "1:11983:7", "1:11984:7", "1:12001:7", "1:12005:7",
        "1:12680:10", "1:12682:8", "1:19334:5", "1:19336:6", "1:19364:5", "1:19365:5", "1:19373:5", "1:19374:5",
        "1:19375:5", "1:19376:5", "1:19377:5", "1:19378:5", "1:19379:5", "1:19380:5", "1:19381:5", "1:19382:5", "1:19384:5",
        "1:19385:5", "1:19386:5", "1:19387:5", "1:19388:5", "1:20305:4", "1:20306:4", "1:20311:4", "1:20312:4", "1:20313:4",
        "1:20314:4", "1:20315:4", "1:20318:4", "1:20319:4", "1:20321:6", "1:20323:4", "1:20325:4", "1:20327:4", "1:20329:4",
        "1:20332:4", "1:20333:4", "1:20335:6", "1:20337:4", "1:20339:4", "1:20341:5", "1:20343:4", "1:20345:4", "1:20349:6",
        "1:20351:4", "1:20352:4", "1:20353:4", "1:20354:4", "1:20355:4", "1:20357:6", "1:20359:4", "1:20361:4", "1:20364:4",
        "1:20365:4", "1:20367:6", "1:20371:4", "1:20373:4", "1:20375:4", "1:20376:4", "1:20379:4", "1:20380:4", "1:20381:8",
        "1:20382:4", "1:20383:4", "1:20384:4", "1:20385:4", "1:20386:4", "1:20389:4", "1:20424:4", "1:51494:3", "1:52087:2",
        "1:60448:1",
    }

    sip_stutter_rules = {
        # sip_voip
        "1:60447:1",
    }

    sip_duplicate_rules = {
        # sip_voip
        InterRulesIssue('1:11976:9', '1:20300:4'), InterRulesIssue('1:11977:9', '1:20301:4'),
        InterRulesIssue('1:11979:7', '1:20382:4'), InterRulesIssue('1:11980:9', '1:20389:4'),
        InterRulesIssue('1:11983:7', '1:20383:4'), InterRulesIssue('1:11984:7', '1:20384:4'),
        InterRulesIssue('1:12001:7', '1:20385:4'), InterRulesIssue('1:12005:7', '1:20386:4'),
        InterRulesIssue('1:19364:5', '1:19365:5'), InterRulesIssue('1:19373:5', '1:19374:5'),
        InterRulesIssue('1:19375:5', '1:19376:5'), InterRulesIssue('1:19377:5', '1:19378:5'),
        InterRulesIssue('1:19379:5', '1:19380:5'), InterRulesIssue('1:19381:5', '1:19382:5'),
        InterRulesIssue('1:19385:5', '1:19386:5'), InterRulesIssue('1:19387:5', '1:19388:5'),
        InterRulesIssue('1:20318:4', '1:20323:4'), InterRulesIssue('1:20354:4', '1:20359:4'),
        InterRulesIssue('1:51494:3', '1:51749:3'), InterRulesIssue('1:51504:4', '1:51767:4'),
        InterRulesIssue('1:51508:4', '1:51509:4', '1:51760:4', '1:51761:4'), InterRulesIssue('1:51508:4', '1:51760:4'),
        InterRulesIssue('1:51508:4', '1:51760:4', '1:51761:4'), InterRulesIssue('1:51509:4', '1:51761:4'),
        InterRulesIssue('1:51760:4', '1:51761:4'),
        InterRulesIssue('1:52087:2', '1:52091:2'), InterRulesIssue('1:60447:1', '1:60448:1'),
    }

    sip_overlapping_rules = {
        # sip_voip
        InterRulesIssue('1:11979:7', '1:19364:5'), InterRulesIssue('1:11979:7', '1:19365:5'),
        InterRulesIssue('1:11979:7', '1:19388:5'), InterRulesIssue('1:11980:9', '1:19364:5'),
        InterRulesIssue('1:11980:9', '1:19365:5'), InterRulesIssue('1:11983:7', '1:19364:5'),
        InterRulesIssue('1:11983:7', '1:19365:5'), InterRulesIssue('1:11984:7', '1:19364:5'),
        InterRulesIssue('1:11984:7', '1:19365:5'), InterRulesIssue('1:12001:7', '1:19364:5'),
        InterRulesIssue('1:12001:7', '1:19365:5'), InterRulesIssue('1:12005:7', '1:19364:5'),
        InterRulesIssue('1:12005:7', '1:19365:5'), InterRulesIssue('1:12682:8', '1:20337:4'),
        InterRulesIssue('1:12682:8', '1:20341:5'), InterRulesIssue('1:16351:11', '1:20305:4'),
        InterRulesIssue('1:16351:11', '1:20306:4'), InterRulesIssue('1:19364:5', '1:19373:5'),
        InterRulesIssue('1:19364:5', '1:19374:5'), InterRulesIssue('1:19364:5', '1:19375:5'),
        InterRulesIssue('1:19364:5', '1:19376:5'), InterRulesIssue('1:19364:5', '1:19377:5'),
        InterRulesIssue('1:19364:5', '1:19378:5'), InterRulesIssue('1:19364:5', '1:19379:5'),
        InterRulesIssue('1:19364:5', '1:19380:5'), InterRulesIssue('1:19364:5', '1:19381:5'),
        InterRulesIssue('1:19364:5', '1:19382:5'), InterRulesIssue('1:19364:5', '1:19384:5'),
        InterRulesIssue('1:19364:5', '1:19385:5'), InterRulesIssue('1:19364:5', '1:19386:5'),
        InterRulesIssue('1:19364:5', '1:19387:5'), InterRulesIssue('1:19364:5', '1:19388:5'),
        InterRulesIssue('1:19364:5', '1:20382:4'), InterRulesIssue('1:19364:5', '1:20383:4'),
        InterRulesIssue('1:19364:5', '1:20384:4'), InterRulesIssue('1:19364:5', '1:20385:4'),
        InterRulesIssue('1:19364:5', '1:20386:4'), InterRulesIssue('1:19364:5', '1:20389:4'),
        InterRulesIssue('1:19365:5', '1:19373:5'), InterRulesIssue('1:19365:5', '1:19374:5'),
        InterRulesIssue('1:19365:5', '1:19375:5'), InterRulesIssue('1:19365:5', '1:19376:5'),
        InterRulesIssue('1:19365:5', '1:19377:5'), InterRulesIssue('1:19365:5', '1:19378:5'),
        InterRulesIssue('1:19365:5', '1:19379:5'), InterRulesIssue('1:19365:5', '1:19380:5'),
        InterRulesIssue('1:19365:5', '1:19381:5'), InterRulesIssue('1:19365:5', '1:19382:5'),
        InterRulesIssue('1:19365:5', '1:19384:5'), InterRulesIssue('1:19365:5', '1:19385:5'),
        InterRulesIssue('1:19365:5', '1:19386:5'), InterRulesIssue('1:19365:5', '1:19387:5'),
        InterRulesIssue('1:19365:5', '1:19388:5'), InterRulesIssue('1:19365:5', '1:20382:4'),
        InterRulesIssue('1:19365:5', '1:20383:4'), InterRulesIssue('1:19365:5', '1:20384:4'),
        InterRulesIssue('1:19365:5', '1:20385:4'), InterRulesIssue('1:19365:5', '1:20386:4'),
        InterRulesIssue('1:19365:5', '1:20389:4'), InterRulesIssue('1:19374:5', '1:19375:5'),
        InterRulesIssue('1:19374:5', '1:19376:5'), InterRulesIssue('1:19379:5', '1:19384:5'),
        InterRulesIssue('1:19380:5', '1:19382:5'), InterRulesIssue('1:19380:5', '1:19384:5'),
        InterRulesIssue('1:19381:5', '1:19384:5'), InterRulesIssue('1:19382:5', '1:19384:5'),
        InterRulesIssue('1:19385:5', '1:19388:5'), InterRulesIssue('1:19386:5', '1:19388:5'),
        InterRulesIssue('1:19388:5', '1:20382:4'), InterRulesIssue('1:20305:4', '1:20306:4'),
        InterRulesIssue('1:20319:4', '1:20321:6'), InterRulesIssue('1:20319:4', '1:20323:4'),
        InterRulesIssue('1:20319:4', '1:20325:4'), InterRulesIssue('1:20319:4', '1:20327:4'),
        InterRulesIssue('1:20319:4', '1:20329:4'), InterRulesIssue('1:20321:6', '1:20329:4'),
        InterRulesIssue('1:20323:4', '1:20327:4'), InterRulesIssue('1:20323:4', '1:20329:4'),
        InterRulesIssue('1:20325:4', '1:20327:4'), InterRulesIssue('1:20333:4', '1:20337:4'),
        InterRulesIssue('1:20333:4', '1:20339:4'), InterRulesIssue('1:20333:4', '1:20341:5'),
        InterRulesIssue('1:20333:4', '1:20343:4'), InterRulesIssue('1:20333:4', '1:20345:4'),
        InterRulesIssue('1:20335:6', '1:20345:4'), InterRulesIssue('1:20337:4', '1:20339:4'),
        InterRulesIssue('1:20337:4', '1:20341:5'), InterRulesIssue('1:20337:4', '1:20343:4'),
        InterRulesIssue('1:20339:4', '1:20341:5'), InterRulesIssue('1:20339:4', '1:20345:4'),
        InterRulesIssue('1:20341:5', '1:20343:4'), InterRulesIssue('1:20354:4', '1:20355:4'),
        InterRulesIssue('1:20355:4', '1:20361:4'), InterRulesIssue('1:51504:4', '1:51508:4'),
        InterRulesIssue('1:51504:4', '1:51509:4'), InterRulesIssue('1:51504:4', '1:51760:4'),
        InterRulesIssue('1:51504:4', '1:51761:4'), InterRulesIssue('1:51504:4', '1:51772:2'),
        InterRulesIssue('1:51508:4', '1:51767:4'), InterRulesIssue('1:51508:4', '1:51772:2'),
        InterRulesIssue('1:51509:4', '1:51767:4'), InterRulesIssue('1:51509:4', '1:51772:2'),
        InterRulesIssue('1:51760:4', '1:51767:4'), InterRulesIssue('1:51760:4', '1:51772:2'),
        InterRulesIssue('1:51761:4', '1:51767:4'), InterRulesIssue('1:51761:4', '1:51772:2'),
        InterRulesIssue('1:51767:4', '1:51772:2'),
    }

    sip_orthogonal_rules = {
        # sip_voip
        InterRulesIssue('1:11976:9', '1:19364:5'), InterRulesIssue('1:11976:9', '1:19365:5'),
        InterRulesIssue('1:11976:9', '1:20300:4'), InterRulesIssue('1:11977:9', '1:19364:5'),
        InterRulesIssue('1:11977:9', '1:19365:5'), InterRulesIssue('1:11977:9', '1:20301:4'),
        InterRulesIssue('1:11979:7', '1:20382:4'), InterRulesIssue('1:11980:9', '1:20389:4'),
        InterRulesIssue('1:11983:7', '1:20383:4'), InterRulesIssue('1:11984:7', '1:20384:4'),
        InterRulesIssue('1:12001:7', '1:20385:4'), InterRulesIssue('1:12005:7', '1:20386:4'),
        InterRulesIssue('1:12680:10', '1:51760:4'), InterRulesIssue('1:12680:10', '1:51761:4'),
        InterRulesIssue('1:12680:10', '1:51767:4'), InterRulesIssue('1:12680:10', '1:51772:2'),
        InterRulesIssue('1:12682:8', '1:51761:4'), InterRulesIssue('1:12682:8', '1:51767:4'),
        InterRulesIssue('1:12682:8', '1:51772:2'), InterRulesIssue('1:16351:11', '1:51508:4'),
        InterRulesIssue('1:16351:11', '1:51509:4'), InterRulesIssue('1:16351:11', '1:51760:4'),
        InterRulesIssue('1:16351:11', '1:51761:4'), InterRulesIssue('1:16351:11', '1:51772:2'),
        InterRulesIssue('1:19334:5', '1:51760:4'), InterRulesIssue('1:19334:5', '1:51761:4'),
        InterRulesIssue('1:19334:5', '1:51767:4'), InterRulesIssue('1:19334:5', '1:51772:2'),
        InterRulesIssue('1:19336:6', '1:51760:4'), InterRulesIssue('1:19336:6', '1:51761:4'),
        InterRulesIssue('1:19336:6', '1:51767:4'), InterRulesIssue('1:19336:6', '1:51772:2'),
        InterRulesIssue('1:19364:5', '1:19365:5'), InterRulesIssue('1:19364:5', '1:20300:4'),
        InterRulesIssue('1:19364:5', '1:20301:4'), InterRulesIssue('1:19364:5', '1:20308:4'),
        InterRulesIssue('1:19364:5', '1:51494:3'), InterRulesIssue('1:19364:5', '1:51749:3'),
        InterRulesIssue('1:19364:5', '1:52087:2'), InterRulesIssue('1:19364:5', '1:52091:2'),
        InterRulesIssue('1:19364:5', '1:60447:1'), InterRulesIssue('1:19364:5', '1:60448:1'),
        InterRulesIssue('1:19365:5', '1:20300:4'), InterRulesIssue('1:19365:5', '1:20301:4'),
        InterRulesIssue('1:19365:5', '1:20308:4'), InterRulesIssue('1:19365:5', '1:51494:3'),
        InterRulesIssue('1:19365:5', '1:51749:3'), InterRulesIssue('1:19365:5', '1:52087:2'),
        InterRulesIssue('1:19365:5', '1:52091:2'), InterRulesIssue('1:19365:5', '1:60447:1'),
        InterRulesIssue('1:19365:5', '1:60448:1'), InterRulesIssue('1:19373:5', '1:19374:5'),
        InterRulesIssue('1:19375:5', '1:19376:5'), InterRulesIssue('1:19377:5', '1:19378:5'),
        InterRulesIssue('1:19379:5', '1:19380:5'), InterRulesIssue('1:19381:5', '1:19382:5'),
        InterRulesIssue('1:19385:5', '1:19386:5'), InterRulesIssue('1:19387:5', '1:19388:5'),
        InterRulesIssue('1:20305:4', '1:51760:4'), InterRulesIssue('1:20305:4', '1:51761:4'),
        InterRulesIssue('1:20305:4', '1:51772:2'), InterRulesIssue('1:20305:4', '1:52093:1'),
        InterRulesIssue('1:20306:4', '1:51760:4'), InterRulesIssue('1:20306:4', '1:51761:4'),
        InterRulesIssue('1:20306:4', '1:51772:2'), InterRulesIssue('1:20306:4', '1:52093:1'),
        InterRulesIssue('1:20311:4', '1:51760:4'), InterRulesIssue('1:20311:4', '1:51761:4'),
        InterRulesIssue('1:20311:4', '1:51767:4'), InterRulesIssue('1:20311:4', '1:51772:2'),
        InterRulesIssue('1:20312:4', '1:51760:4'), InterRulesIssue('1:20312:4', '1:51761:4'),
        InterRulesIssue('1:20312:4', '1:51767:4'), InterRulesIssue('1:20312:4', '1:51772:2'),
        InterRulesIssue('1:20313:4', '1:51760:4'), InterRulesIssue('1:20313:4', '1:51761:4'),
        InterRulesIssue('1:20313:4', '1:51767:4'), InterRulesIssue('1:20313:4', '1:51772:2'),
        InterRulesIssue('1:20314:4', '1:51760:4'), InterRulesIssue('1:20314:4', '1:51761:4'),
        InterRulesIssue('1:20314:4', '1:51767:4'), InterRulesIssue('1:20314:4', '1:51772:2'),
        InterRulesIssue('1:20315:4', '1:51760:4'), InterRulesIssue('1:20315:4', '1:51761:4'),
        InterRulesIssue('1:20315:4', '1:51767:4'), InterRulesIssue('1:20315:4', '1:51772:2'),
        InterRulesIssue('1:20318:4', '1:20323:4'), InterRulesIssue('1:20318:4', '1:51760:4'),
        InterRulesIssue('1:20318:4', '1:51767:4'), InterRulesIssue('1:20318:4', '1:51772:2'),
        InterRulesIssue('1:20319:4', '1:20424:4'), InterRulesIssue('1:20319:4', '1:51760:4'),
        InterRulesIssue('1:20319:4', '1:51767:4'), InterRulesIssue('1:20319:4', '1:51772:2'),
        InterRulesIssue('1:20321:6', '1:51760:4'), InterRulesIssue('1:20321:6', '1:51767:4'),
        InterRulesIssue('1:20321:6', '1:51772:2'), InterRulesIssue('1:20323:4', '1:51760:4'),
        InterRulesIssue('1:20323:4', '1:51767:4'), InterRulesIssue('1:20323:4', '1:51772:2'),
        InterRulesIssue('1:20325:4', '1:51760:4'), InterRulesIssue('1:20325:4', '1:51767:4'),
        InterRulesIssue('1:20325:4', '1:51772:2'), InterRulesIssue('1:20327:4', '1:51760:4'),
        InterRulesIssue('1:20327:4', '1:51767:4'), InterRulesIssue('1:20327:4', '1:51772:2'),
        InterRulesIssue('1:20329:4', '1:51760:4'), InterRulesIssue('1:20329:4', '1:51767:4'),
        InterRulesIssue('1:20329:4', '1:51772:2'), InterRulesIssue('1:20332:4', '1:20337:4'),
        InterRulesIssue('1:20332:4', '1:51761:4'), InterRulesIssue('1:20332:4', '1:51767:4'),
        InterRulesIssue('1:20332:4', '1:51772:2'), InterRulesIssue('1:20333:4', '1:20335:6'),
        InterRulesIssue('1:20333:4', '1:51761:4'), InterRulesIssue('1:20333:4', '1:51767:4'),
        InterRulesIssue('1:20333:4', '1:51772:2'), InterRulesIssue('1:20335:6', '1:51761:4'),
        InterRulesIssue('1:20335:6', '1:51767:4'), InterRulesIssue('1:20335:6', '1:51772:2'),
        InterRulesIssue('1:20337:4', '1:51761:4'), InterRulesIssue('1:20337:4', '1:51767:4'),
        InterRulesIssue('1:20337:4', '1:51772:2'), InterRulesIssue('1:20339:4', '1:51761:4'),
        InterRulesIssue('1:20339:4', '1:51767:4'), InterRulesIssue('1:20339:4', '1:51772:2'),
        InterRulesIssue('1:20341:5', '1:51761:4'), InterRulesIssue('1:20341:5', '1:51767:4'),
        InterRulesIssue('1:20341:5', '1:51772:2'), InterRulesIssue('1:20343:4', '1:51761:4'),
        InterRulesIssue('1:20343:4', '1:51767:4'), InterRulesIssue('1:20343:4', '1:51772:2'),
        InterRulesIssue('1:20345:4', '1:51761:4'), InterRulesIssue('1:20345:4', '1:51767:4'),
        InterRulesIssue('1:20345:4', '1:51772:2'), InterRulesIssue('1:20349:6', '1:51760:4'),
        InterRulesIssue('1:20349:6', '1:51761:4'), InterRulesIssue('1:20349:6', '1:51767:4'),
        InterRulesIssue('1:20349:6', '1:51772:2'), InterRulesIssue('1:20351:4', '1:51760:4'),
        InterRulesIssue('1:20351:4', '1:51761:4'), InterRulesIssue('1:20351:4', '1:51767:4'),
        InterRulesIssue('1:20351:4', '1:51772:2'), InterRulesIssue('1:20352:4', '1:51760:4'),
        InterRulesIssue('1:20352:4', '1:51761:4'), InterRulesIssue('1:20352:4', '1:51767:4'),
        InterRulesIssue('1:20352:4', '1:51772:2'), InterRulesIssue('1:20353:4', '1:51760:4'),
        InterRulesIssue('1:20353:4', '1:51761:4'), InterRulesIssue('1:20353:4', '1:51767:4'),
        InterRulesIssue('1:20353:4', '1:51772:2'), InterRulesIssue('1:20354:4', '1:20359:4'),
        InterRulesIssue('1:20354:4', '1:51760:4'), InterRulesIssue('1:20354:4', '1:51761:4'),
        InterRulesIssue('1:20354:4', '1:51767:4'), InterRulesIssue('1:20355:4', '1:20357:6'),
        InterRulesIssue('1:20355:4', '1:51760:4'), InterRulesIssue('1:20355:4', '1:51761:4'),
        InterRulesIssue('1:20355:4', '1:51767:4'), InterRulesIssue('1:20357:6', '1:51760:4'),
        InterRulesIssue('1:20357:6', '1:51761:4'), InterRulesIssue('1:20357:6', '1:51767:4'),
        InterRulesIssue('1:20359:4', '1:51760:4'), InterRulesIssue('1:20359:4', '1:51761:4'),
        InterRulesIssue('1:20359:4', '1:51767:4'), InterRulesIssue('1:20361:4', '1:51760:4'),
        InterRulesIssue('1:20361:4', '1:51761:4'), InterRulesIssue('1:20361:4', '1:51767:4'),
        InterRulesIssue('1:20364:4', '1:51760:4'), InterRulesIssue('1:20364:4', '1:51761:4'),
        InterRulesIssue('1:20364:4', '1:51767:4'), InterRulesIssue('1:20364:4', '1:51772:2'),
        InterRulesIssue('1:20365:4', '1:51760:4'), InterRulesIssue('1:20365:4', '1:51761:4'),
        InterRulesIssue('1:20365:4', '1:51767:4'), InterRulesIssue('1:20365:4', '1:51772:2'),
        InterRulesIssue('1:20367:6', '1:51760:4'), InterRulesIssue('1:20367:6', '1:51761:4'),
        InterRulesIssue('1:20367:6', '1:51767:4'), InterRulesIssue('1:20367:6', '1:51772:2'),
        InterRulesIssue('1:20371:4', '1:51760:4'), InterRulesIssue('1:20371:4', '1:51761:4'),
        InterRulesIssue('1:20371:4', '1:51767:4'), InterRulesIssue('1:20371:4', '1:51772:2'),
        InterRulesIssue('1:20373:4', '1:51760:4'), InterRulesIssue('1:20373:4', '1:51761:4'),
        InterRulesIssue('1:20373:4', '1:51767:4'), InterRulesIssue('1:20373:4', '1:51772:2'),
        InterRulesIssue('1:20375:4', '1:51760:4'), InterRulesIssue('1:20375:4', '1:51761:4'),
        InterRulesIssue('1:20375:4', '1:51767:4'), InterRulesIssue('1:20375:4', '1:51772:2'),
        InterRulesIssue('1:20376:4', '1:51760:4'), InterRulesIssue('1:20376:4', '1:51761:4'),
        InterRulesIssue('1:20376:4', '1:51767:4'), InterRulesIssue('1:20376:4', '1:51772:2'),
        InterRulesIssue('1:20377:4', '1:51760:4'), InterRulesIssue('1:20377:4', '1:51761:4'),
        InterRulesIssue('1:20377:4', '1:51767:4'), InterRulesIssue('1:20377:4', '1:51772:2'),
        InterRulesIssue('1:20379:4', '1:51760:4'), InterRulesIssue('1:20379:4', '1:51761:4'),
        InterRulesIssue('1:20379:4', '1:51767:4'), InterRulesIssue('1:20379:4', '1:51772:2'),
        InterRulesIssue('1:20380:4', '1:51760:4'), InterRulesIssue('1:20380:4', '1:51761:4'),
        InterRulesIssue('1:20380:4', '1:51767:4'), InterRulesIssue('1:20380:4', '1:51772:2'),
        InterRulesIssue('1:20381:8', '1:51760:4'), InterRulesIssue('1:20381:8', '1:51761:4'),
        InterRulesIssue('1:20381:8', '1:51767:4'), InterRulesIssue('1:20381:8', '1:51772:2'),
        InterRulesIssue('1:20424:4', '1:51760:4'), InterRulesIssue('1:20424:4', '1:51767:4'),
        InterRulesIssue('1:20424:4', '1:51772:2'), InterRulesIssue('1:51494:3', '1:51749:3'),
        InterRulesIssue('1:51504:4', '1:51767:4'), InterRulesIssue('1:51508:4', '1:51509:4'),
        InterRulesIssue('1:51508:4', '1:51760:4'), InterRulesIssue('1:51508:4', '1:51761:4'),
        InterRulesIssue('1:51508:4', '1:52093:1'), InterRulesIssue('1:51509:4', '1:51760:4'),
        InterRulesIssue('1:51509:4', '1:51761:4'), InterRulesIssue('1:51509:4', '1:52093:1'),
        InterRulesIssue('1:51760:4', '1:51761:4'), InterRulesIssue('1:51760:4', '1:52093:1'),
        InterRulesIssue('1:51761:4', '1:52093:1'), InterRulesIssue('1:51772:2', '1:52093:1'),
        InterRulesIssue('1:52087:2', '1:52091:2'), InterRulesIssue('1:60447:1', '1:60448:1'),
    }

    ############################################################################################
    ############################################################################################


    http_crude_rules = {
        # http_chrome
        # http_firefox
        "1:43642:4", "1:43761:2",
        # http_webkit
        # http_other
        # http_ie
        # http_plugins
    }

    http_chameleon_rules = {
        # http_chrome
        "1:35412:3", "1:60282:2",
        # http_firefox
        "1:17212:14", "1:18332:6", "1:20072:9", "1:20600:12", "1:30485:2", "1:43761:2", "1:54379:1",
        # http_webkit
        "1:18508:6", "1:23805:8", "1:26658:5",
        # http_other
        "1:24474:2", "1:30958:3", "1:60645:1",
        # http_ie
        "1:13980:17", "1:16033:14", "1:17448:11", "1:17689:12", "1:19670:12", "1:33352:3", "1:35215:3", "1:36988:2",
        "1:37257:3",
        # http_plugins
        "1:18578:11", "1:20709:12", "1:7446:14", "1:8385:14",
    }

    http_stutter_rules = set()

    http_duplicate_rules = {
        # http_chrome
        # http_firefox
        # http_webkit
        # http_other
        # http_ie
        # http_plugins
        InterRulesIssue('1:10193:21', '1:10194:22'), InterRulesIssue('1:10414:10', '1:10417:10'),
        InterRulesIssue('1:11189:14', '1:11201:13'),
        InterRulesIssue('1:13436:13', '1:13444:13'),
    }

    http_overlapping_rules = {
        # http_chrome
        # http_firefox
        # http_webkit
        # http_other
        # http_ie
        InterRulesIssue('1:19873:14', '1:25329:8'), InterRulesIssue('1:26569:4', '1:26668:3'),
        # http_plugins
        InterRulesIssue('1:10191:9', '1:43373:2'), InterRulesIssue('1:11178:15', '1:11189:14'),
        InterRulesIssue('1:11178:15', '1:11201:13'), InterRulesIssue('1:11224:12', '1:37507:3'),
        InterRulesIssue('1:12248:10', '1:12252:10'), InterRulesIssue('1:12450:15', '1:8854:14'),
        InterRulesIssue('1:13446:11', '1:13785:10'),
        InterRulesIssue('1:14326:12', '1:4233:15'), InterRulesIssue('1:15280:9', '1:30048:4'),
        InterRulesIssue('1:16510:15', '1:19893:10'), InterRulesIssue('1:16573:9', '1:17571:9'),
        InterRulesIssue('1:16740:6', '1:20901:6'), InterRulesIssue('1:17160:14', '1:17163:10'),
        InterRulesIssue('1:21030:7', '1:39383:2'), InterRulesIssue('1:21918:13', '1:39167:2'),
        InterRulesIssue('1:23395:13', '1:35327:3'), InterRulesIssue('1:23396:9', '1:35329:3'),
        InterRulesIssue('1:24560:7', '1:29060:7'), InterRulesIssue('1:26364:11', '1:37996:1'),
        InterRulesIssue('1:27206:5', '1:27207:4'), InterRulesIssue('1:28750:6', '1:28759:6'),
        InterRulesIssue('1:28751:6', '1:28760:6'), InterRulesIssue('1:28755:6', '1:28761:6'),
        InterRulesIssue('1:28756:6', '1:28757:6'), InterRulesIssue('1:28765:6', '1:28766:6'),
        InterRulesIssue('1:28768:6', '1:28769:6'), InterRulesIssue('1:28772:6', '1:28787:6'),
        InterRulesIssue('1:28775:6', '1:28788:6'), InterRulesIssue('1:28776:6', '1:28777:6'),
        InterRulesIssue('1:28780:6', '1:28781:6'), InterRulesIssue('1:28784:6', '1:28789:6'),
        InterRulesIssue('1:34639:2', '1:34640:2'), InterRulesIssue('1:34919:3', '1:34922:3'),
        InterRulesIssue('1:37512:2', '1:38435:2'), InterRulesIssue('1:39038:2', '1:41803:2'),
        InterRulesIssue('1:39970:2', '1:45286:2'), InterRulesIssue('1:41491:2', '1:41500:3'),
    }

    http_orthogonal_rules = {
        # http_chrome
        # http_firefox
        # http_webkit
        # http_other
        # http_ie
        InterRulesIssue('1:39219:3', '1:49725:2'), InterRulesIssue('1:39220:3', '1:49725:2'),
        # http_plugins
        InterRulesIssue('1:10193:21', '1:10194:22'), InterRulesIssue('1:10414:10', '1:10417:10'),
        InterRulesIssue('1:11189:14', '1:11201:13'),
        InterRulesIssue('1:11230:11', '1:37040:2'), InterRulesIssue('1:11234:11', '1:37043:2'),
        InterRulesIssue('1:12442:9', '1:43649:2'), InterRulesIssue('1:12604:9', '1:43377:2'),
        InterRulesIssue('1:13260:14', '1:51406:1'), InterRulesIssue('1:13264:14', '1:51407:1'),
        InterRulesIssue('1:13434:14', '1:26974:3'), InterRulesIssue('1:13436:13', '1:13444:13'),
        InterRulesIssue('1:14500:12', '1:7439:16'), InterRulesIssue('1:14765:10', '1:8740:13'),
        InterRulesIssue('1:15245:9', '1:17226:8'), InterRulesIssue('1:15268:9', '1:37022:1'),
        InterRulesIssue('1:16511:14', '1:7004:20'), InterRulesIssue('1:19151:14', '1:19152:13'),
        InterRulesIssue('1:23372:7', '1:36487:3'), InterRulesIssue('1:23374:7', '1:36490:3'),
        InterRulesIssue('1:23376:7', '1:36485:3'), InterRulesIssue('1:24772:6', '1:51408:1'),
        InterRulesIssue('1:24773:9', '1:51410:1'), InterRulesIssue('1:39971:2', '1:45288:2'),
    }

    ############################################################################################
    ############################################################################################



obfuscation_issues = ObfuscateIssues()