from scripts.statistics.InterRulesIssue import InterRulesIssue



class PassThroughIssues:

    ############################################################################################
    ############################################################################################


    dns_crude_rules = set()

    dns_chameleon_rules = {
        # dns_community
        "1:1948:20", "1:253:15", "1:258:17", "1:259:18", "1:260:19", "1:261:16", "1:262:15", "1:264:14", "1:265:16",
        "1:266:15", "1:28556:3", "1:28557:3", "1:2921:12", "1:303:24", "1:314:23", "1:32179:2", "1:45964:1", "1:45966:1",
        "1:45967:2", "1:45968:2", "1:56592:1", "1:56593:1",
        # dns_dns
        "1:17485:9", "1:23368:7", "1:24304:3", "1:253:15", "1:28557:3", "1:32959:3", "1:37015:2", "1:38281:1", "1:38282:1",
        "1:38283:1", "1:38284:1", "1:54630:1", "1:57878:1", "1:59617:1", "1:59859:1",
    }

    dns_stutter_rules = {
        # dns_community
        "1:255:24",
        # dns_dns
        "1:19125:5", "1:24304:3", "1:25333:7", "1:59600:1",
    }

    dns_duplicate_rules = set()

    dns_overlapping_rules = {
        # dns_community
        InterRulesIssue('1:2921:12', '1:2922:12'), InterRulesIssue('1:2921:12', '1:3154:12'),
        InterRulesIssue('1:2922:12', '1:3153:9'), InterRulesIssue('1:56592:1', '1:56593:1'),
        # dns_dns
        InterRulesIssue('1:2922:12', '1:32959:3'),
    }

    dns_orthogonal_rules = {
        # dns_community
        InterRulesIssue('1:2921:12', '1:303:24'), InterRulesIssue('1:2921:12', '1:45964:1'),
        InterRulesIssue('1:2921:12', '1:45966:1'), InterRulesIssue('1:2921:12', '1:45967:2'),
        InterRulesIssue('1:2921:12', '1:45968:2'), InterRulesIssue('1:2921:12', '1:56592:1'),
        InterRulesIssue('1:2921:12', '1:56593:1'), InterRulesIssue('1:2922:12', '1:45964:1'),
        InterRulesIssue('1:2922:12', '1:45966:1'), InterRulesIssue('1:2922:12', '1:45967:2'),
        InterRulesIssue('1:2922:12', '1:45968:2'),
        # dns_dns
        InterRulesIssue('1:19125:5', '1:2921:12'),
    }


    ############################################################################################
    ############################################################################################


    ftp_crude_rules = {
        # ftp_community
        "1:2417:17",
        # ftp_ftp
        "1:1377:24", "1:1378:24", "1:17059:6", "1:2417:17", "1:3441:13",
    }

    ftp_chameleon_rules = {
        # ftp_community
        "1:1378:24", "1:1445:9", "1:1927:8", "1:2272:13", "1:23055:10", "1:2333:9", "1:2574:9", "1:308:14", "1:3441:13",
        "1:3460:9", "1:353:13", "1:354:12", "1:355:13", "1:356:12", "1:357:12", "1:358:12", "1:362:20", "1:38385:3",
        "1:38950:4", "1:43663:2", "1:46335:3", "1:489:19", "1:546:10", "1:548:10",
        # ftp_ftp
        "1:3441:13", "1:45591:3",
    }

    ftp_stutter_rules = {
        # ftp_community
        "1:1377:24", "1:1378:24", "1:21255:6", "1:23055:10", "1:2417:17", "1:32043:3", "1:32069:3", "1:546:10", "1:547:11",
        "1:548:10", "1:554:10",
        # ftp_ftp
        "1:13925:12", "1:16357:7", "1:17059:6", "1:23055:10", "1:2417:17", "1:34225:5", "1:45460:3", "1:45461:2",
        "1:45591:3",
    }

    ftp_duplicate_rules = set()

    ftp_overlapping_rules = {
        # ftp_community
        InterRulesIssue('1:1377:24', '1:1378:24'), InterRulesIssue('1:1672:22', '1:336:17'),
        InterRulesIssue('1:1777:19', '1:1778:18'), InterRulesIssue('1:1971:13', '1:361:22'),
        InterRulesIssue('1:2178:23', '1:553:13'), InterRulesIssue('1:2179:16', '1:489:19'),
        InterRulesIssue('1:23055:10', '1:547:11'), InterRulesIssue('1:2332:10', '1:2417:17'),
        InterRulesIssue('1:2417:17', '1:489:19'), InterRulesIssue('1:336:17', '1:546:10'),
        # ftp_ftp
        InterRulesIssue('1:1377:24', '1:1378:24'), InterRulesIssue('1:14770:11', '1:2417:17'),
        InterRulesIssue('1:14770:11', '1:360:16'), InterRulesIssue('1:1672:22', '1:336:17'),
        InterRulesIssue('1:1971:13', '1:361:22'), InterRulesIssue('1:2332:10', '1:2417:17'),
    }

    ftp_orthogonal_rules = {
        # ftp_community
        InterRulesIssue('1:1377:24', '1:38950:4'), InterRulesIssue('1:1378:24', '1:38950:4'),
        InterRulesIssue('1:2417:17', '1:38950:4'), InterRulesIssue('1:1377:24', '1:23055:10'),
        InterRulesIssue('1:1377:24', '1:2332:10'), InterRulesIssue('1:1377:24', '1:2343:14'),
        InterRulesIssue('1:1377:24', '1:2417:17'), InterRulesIssue('1:1378:24', '1:23055:10'),
        InterRulesIssue('1:1378:24', '1:2332:10'), InterRulesIssue('1:1378:24', '1:2343:14'),
        InterRulesIssue('1:1378:24', '1:2417:17'), InterRulesIssue('1:1672:22', '1:546:10'),
        InterRulesIssue('1:1777:19', '1:2417:17'), InterRulesIssue('1:1778:18', '1:2417:17'),
        InterRulesIssue('1:1971:13', '1:2417:17'), InterRulesIssue('1:2178:23', '1:2417:17'),
        InterRulesIssue('1:2179:16', '1:2417:17'), InterRulesIssue('1:23055:10', '1:2332:10'),
        InterRulesIssue('1:23055:10', '1:2417:17'), InterRulesIssue('1:23055:10', '1:554:10'),
        InterRulesIssue('1:2332:10', '1:547:11'), InterRulesIssue('1:2333:9', '1:2417:17'),
        InterRulesIssue('1:2343:14', '1:2417:17'), InterRulesIssue('1:2417:17', '1:2574:9'),
        InterRulesIssue('1:2417:17', '1:361:22'), InterRulesIssue('1:2417:17', '1:545:9'),
        InterRulesIssue('1:2417:17', '1:547:11'), InterRulesIssue('1:2417:17', '1:553:13'),
        InterRulesIssue('1:2417:17', '1:554:10'),
        # ftp_ftp
        InterRulesIssue('1:1377:24', '1:23055:10'), InterRulesIssue('1:1377:24', '1:2343:14'),
        InterRulesIssue('1:1377:24', '1:2417:17'), InterRulesIssue('1:1377:24', '1:26471:9'),
        InterRulesIssue('1:1377:24', '1:39378:2'), InterRulesIssue('1:1377:24', '1:45591:3'),
        InterRulesIssue('1:1378:24', '1:2343:14'), InterRulesIssue('1:1378:24', '1:2417:17'),
        InterRulesIssue('1:1378:24', '1:26471:9'), InterRulesIssue('1:1378:24', '1:39378:2'),
        InterRulesIssue('1:1378:24', '1:45591:3'), InterRulesIssue('1:14770:11', '1:16357:7'),
        InterRulesIssue('1:14770:11', '1:2343:14'), InterRulesIssue('1:14770:11', '1:45828:1'),
        InterRulesIssue('1:16524:10', '1:2417:17'), InterRulesIssue('1:17059:6', '1:2417:17'),
        InterRulesIssue('1:17059:6', '1:3441:13'), InterRulesIssue('1:17059:6', '1:8480:12'),
        InterRulesIssue('1:17329:8', '1:2417:17'), InterRulesIssue('1:1971:13', '1:2417:17'),
        InterRulesIssue('1:2178:23', '1:2417:17'), InterRulesIssue('1:2179:16', '1:2417:17'),
        InterRulesIssue('1:2333:9', '1:2417:17'), InterRulesIssue('1:2343:14', '1:2417:17'),
        InterRulesIssue('1:2417:17', '1:2574:9'), InterRulesIssue('1:2417:17', '1:26471:9'),
        InterRulesIssue('1:2417:17', '1:3441:13'), InterRulesIssue('1:2417:17', '1:3523:11'),
        InterRulesIssue('1:2417:17', '1:361:22'), InterRulesIssue('1:2417:17', '1:39378:2'),
        InterRulesIssue('1:2417:17', '1:45591:3'), InterRulesIssue('1:2417:17', '1:8480:12'),
        InterRulesIssue('1:3441:13', '1:8480:12'),
    }


    ############################################################################################
    ############################################################################################


    sip_crude_rules = {
        # sip_voip
        "1:11980:9", "1:19364:5", "1:19365:5", "1:20313:4", "1:20319:4", "1:20333:4", "1:20337:4", "1:20365:4", "1:20389:4",
        "1:51504:4", "1:51508:4", "1:51509:4", "1:51744:2", "1:51760:4", "1:51761:4", "1:51767:4", "1:51772:2", "1:52090:1",
        "1:52093:1",

    }

    sip_chameleon_rules = {
        # sip_voip
        "1:11976:9", "1:11977:9", "1:11979:7", "1:11980:9", "1:11983:7", "1:11984:7", "1:12001:7", "1:12005:7", "1:12682:8",
        "1:19334:5", "1:19336:6", "1:19364:5", "1:19365:5", "1:19373:5", "1:19374:5", "1:19375:5", "1:19376:5", "1:19377:5",
        "1:19378:5", "1:19379:5", "1:19380:5", "1:19381:5", "1:19382:5", "1:19383:5", "1:19384:5", "1:19385:5", "1:19386:5",
        "1:19387:5", "1:19388:5", "1:20305:4", "1:20306:4", "1:20311:4", "1:20312:4", "1:20313:4", "1:20314:4", "1:20315:4",
        "1:20318:4", "1:20319:4", "1:20321:6", "1:20323:4", "1:20325:4", "1:20327:4", "1:20329:4", "1:20332:4", "1:20333:4",
        "1:20335:6", "1:20337:4", "1:20339:4", "1:20341:5", "1:20343:4", "1:20345:4", "1:20349:6", "1:20351:4", "1:20352:4",
        "1:20353:4", "1:20354:4", "1:20355:4", "1:20357:6", "1:20359:4", "1:20361:4", "1:20365:4", "1:20367:6", "1:20371:4",
        "1:20373:4", "1:20375:4", "1:20376:4", "1:20377:4", "1:20379:4", "1:20380:4", "1:20381:8", "1:20382:4", "1:20383:4",
        "1:20384:4", "1:20385:4", "1:20386:4", "1:20389:4", "1:20424:4", "1:21150:6", "1:51492:2", "1:51493:2", "1:51494:3",
        "1:51495:2", "1:51497:2", "1:51499:2", "1:51506:2", "1:51512:2", "1:51513:2", "1:51515:2", "1:51745:2", "1:52087:2",
        "1:52088:1", "1:52090:1", "1:52326:1", "1:57684:1", "1:60448:1",
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
        InterRulesIssue('1:13693:12', '1:20390:9'), InterRulesIssue('1:19364:5', '1:19365:5'),
        InterRulesIssue('1:19373:5', '1:19374:5'), InterRulesIssue('1:19375:5', '1:19376:5'),
        InterRulesIssue('1:19377:5', '1:19378:5'), InterRulesIssue('1:19379:5', '1:19380:5'),
        InterRulesIssue('1:19381:5', '1:19382:5'), InterRulesIssue('1:19383:5', '1:19384:5'),
        InterRulesIssue('1:19385:5', '1:19386:5'), InterRulesIssue('1:19387:5', '1:19388:5'),
        InterRulesIssue('1:20318:4', '1:20323:4'), InterRulesIssue('1:20354:4', '1:20359:4'),
        InterRulesIssue('1:51492:2', '1:51747:2'), InterRulesIssue('1:51493:2', '1:51750:2'),
        InterRulesIssue('1:51494:3', '1:51749:3'), InterRulesIssue('1:51495:2', '1:51751:2'),
        InterRulesIssue('1:51497:2', '1:51753:2'), InterRulesIssue('1:51499:2', '1:51754:2'),
        InterRulesIssue('1:51504:4', '1:51767:4'), InterRulesIssue('1:51506:2', '1:51758:2'),
        InterRulesIssue('1:51508:4', '1:51509:4', '1:51760:4', '1:51761:4'), InterRulesIssue('1:51508:4', '1:51760:4'),
        InterRulesIssue('1:51509:4', '1:51761:4'),
        InterRulesIssue('1:51512:2', '1:51771:2'), InterRulesIssue('1:51513:2', '1:51769:2'),
        InterRulesIssue('1:51515:2', '1:51770:2'), InterRulesIssue('1:51744:2', '1:51772:2'),
        InterRulesIssue('1:51745:2', '1:51773:2'), InterRulesIssue('1:51760:4', '1:51761:4'),
        InterRulesIssue('1:52087:2', '1:52091:2'), InterRulesIssue('1:52088:1', '1:52092:1'),
        InterRulesIssue('1:52090:1', '1:52093:1'), InterRulesIssue('1:52326:1', '1:52327:1'),
        InterRulesIssue('1:57683:1', '1:57684:1'), InterRulesIssue('1:60447:1', '1:60448:1'),
    }

    sip_overlapping_rules = {
        # sip_voip
        InterRulesIssue('1:11979:7', '1:19364:5'), InterRulesIssue('1:11979:7', '1:19365:5'),
        InterRulesIssue('1:11980:9', '1:19364:5'), InterRulesIssue('1:11980:9', '1:19365:5'),
        InterRulesIssue('1:11983:7', '1:19364:5'), InterRulesIssue('1:11983:7', '1:19365:5'),
        InterRulesIssue('1:11984:7', '1:19364:5'), InterRulesIssue('1:11984:7', '1:19365:5'),
        InterRulesIssue('1:12001:7', '1:19364:5'), InterRulesIssue('1:12001:7', '1:19365:5'),
        InterRulesIssue('1:12005:7', '1:19364:5'), InterRulesIssue('1:12005:7', '1:19365:5'),
        InterRulesIssue('1:12682:8', '1:20337:4'), InterRulesIssue('1:16351:11', '1:20305:4'),
        InterRulesIssue('1:16351:11', '1:20306:4'), InterRulesIssue('1:19364:5', '1:19373:5'),
        InterRulesIssue('1:19364:5', '1:19374:5'), InterRulesIssue('1:19364:5', '1:19375:5'),
        InterRulesIssue('1:19364:5', '1:19376:5'), InterRulesIssue('1:19364:5', '1:19377:5'),
        InterRulesIssue('1:19364:5', '1:19378:5'), InterRulesIssue('1:19364:5', '1:19379:5'),
        InterRulesIssue('1:19364:5', '1:19380:5'), InterRulesIssue('1:19364:5', '1:19381:5'),
        InterRulesIssue('1:19364:5', '1:19382:5'), InterRulesIssue('1:19364:5', '1:19383:5'),
        InterRulesIssue('1:19364:5', '1:19384:5'), InterRulesIssue('1:19364:5', '1:19385:5'),
        InterRulesIssue('1:19364:5', '1:19386:5'), InterRulesIssue('1:19364:5', '1:19387:5'),
        InterRulesIssue('1:19364:5', '1:19388:5'), InterRulesIssue('1:19364:5', '1:20382:4'),
        InterRulesIssue('1:19364:5', '1:20383:4'), InterRulesIssue('1:19364:5', '1:20384:4'),
        InterRulesIssue('1:19364:5', '1:20385:4'), InterRulesIssue('1:19364:5', '1:20386:4'),
        InterRulesIssue('1:19364:5', '1:20389:4'), InterRulesIssue('1:19364:5', '1:51493:2'),
        InterRulesIssue('1:19364:5', '1:51497:2'), InterRulesIssue('1:19364:5', '1:51750:2'),
        InterRulesIssue('1:19364:5', '1:51753:2'), InterRulesIssue('1:19365:5', '1:19373:5'),
        InterRulesIssue('1:19365:5', '1:19374:5'), InterRulesIssue('1:19365:5', '1:19375:5'),
        InterRulesIssue('1:19365:5', '1:19376:5'), InterRulesIssue('1:19365:5', '1:19377:5'),
        InterRulesIssue('1:19365:5', '1:19378:5'), InterRulesIssue('1:19365:5', '1:19379:5'),
        InterRulesIssue('1:19365:5', '1:19380:5'), InterRulesIssue('1:19365:5', '1:19381:5'),
        InterRulesIssue('1:19365:5', '1:19382:5'), InterRulesIssue('1:19365:5', '1:19383:5'),
        InterRulesIssue('1:19365:5', '1:19384:5'), InterRulesIssue('1:19365:5', '1:19385:5'),
        InterRulesIssue('1:19365:5', '1:19386:5'), InterRulesIssue('1:19365:5', '1:19387:5'),
        InterRulesIssue('1:19365:5', '1:19388:5'), InterRulesIssue('1:19365:5', '1:20382:4'),
        InterRulesIssue('1:19365:5', '1:20383:4'), InterRulesIssue('1:19365:5', '1:20384:4'),
        InterRulesIssue('1:19365:5', '1:20385:4'), InterRulesIssue('1:19365:5', '1:20386:4'),
        InterRulesIssue('1:19365:5', '1:20389:4'), InterRulesIssue('1:19365:5', '1:51493:2'),
        InterRulesIssue('1:19365:5', '1:51497:2'), InterRulesIssue('1:19365:5', '1:51750:2'),
        InterRulesIssue('1:19365:5', '1:51753:2'), InterRulesIssue('1:19373:5', '1:19375:5'),
        InterRulesIssue('1:19373:5', '1:19376:5'), InterRulesIssue('1:19374:5', '1:19375:5'),
        InterRulesIssue('1:19374:5', '1:19376:5'), InterRulesIssue('1:19380:5', '1:19381:5'),
        InterRulesIssue('1:19380:5', '1:19382:5'), InterRulesIssue('1:19380:5', '1:19383:5'),
        InterRulesIssue('1:19380:5', '1:19384:5'), InterRulesIssue('1:19382:5', '1:19383:5'),
        InterRulesIssue('1:19382:5', '1:19384:5'), InterRulesIssue('1:19385:5', '1:19387:5'),
        InterRulesIssue('1:19385:5', '1:19388:5'), InterRulesIssue('1:19386:5', '1:19387:5'),
        InterRulesIssue('1:19386:5', '1:19388:5'), InterRulesIssue('1:20305:4', '1:20306:4'),
        InterRulesIssue('1:20319:4', '1:20321:6'), InterRulesIssue('1:20319:4', '1:20325:4'),
        InterRulesIssue('1:20319:4', '1:20327:4'), InterRulesIssue('1:20319:4', '1:20329:4'),
        InterRulesIssue('1:20321:6', '1:20329:4'), InterRulesIssue('1:20325:4', '1:20327:4'),
        InterRulesIssue('1:20333:4', '1:20337:4'), InterRulesIssue('1:20333:4', '1:20341:5'),
        InterRulesIssue('1:20333:4', '1:20343:4'), InterRulesIssue('1:20333:4', '1:20345:4'),
        InterRulesIssue('1:20335:6', '1:20345:4'), InterRulesIssue('1:20337:4', '1:20339:4'),
        InterRulesIssue('1:20337:4', '1:20341:5'), InterRulesIssue('1:20337:4', '1:20343:4'),
        InterRulesIssue('1:20337:4', '1:20345:4'), InterRulesIssue('1:20339:4', '1:20341:5'),
        InterRulesIssue('1:20341:5', '1:20343:4'), InterRulesIssue('1:20355:4', '1:20361:4'),
        InterRulesIssue('1:51504:4', '1:51508:4'), InterRulesIssue('1:51504:4', '1:51509:4'),
        InterRulesIssue('1:51504:4', '1:51744:2'), InterRulesIssue('1:51504:4', '1:51760:4'),
        InterRulesIssue('1:51504:4', '1:51761:4'), InterRulesIssue('1:51504:4', '1:51772:2'),
        InterRulesIssue('1:51508:4', '1:51744:2'), InterRulesIssue('1:51508:4', '1:51767:4'),
        InterRulesIssue('1:51508:4', '1:51772:2'), InterRulesIssue('1:51509:4', '1:51744:2'),
        InterRulesIssue('1:51509:4', '1:51767:4'), InterRulesIssue('1:51509:4', '1:51772:2'),
        InterRulesIssue('1:51744:2', '1:51760:4'), InterRulesIssue('1:51744:2', '1:51761:4'),
        InterRulesIssue('1:51744:2', '1:51767:4'), InterRulesIssue('1:51760:4', '1:51767:4'),
        InterRulesIssue('1:51760:4', '1:51772:2'), InterRulesIssue('1:51761:4', '1:51767:4'),
        InterRulesIssue('1:51761:4', '1:51772:2'), InterRulesIssue('1:51767:4', '1:51772:2'),
    }

    sip_orthogonal_rules = {
        # sip_voip
        InterRulesIssue('1:11976:9', '1:19364:5'), InterRulesIssue('1:11976:9', '1:19365:5'),
        InterRulesIssue('1:11976:9', '1:20300:4'), InterRulesIssue('1:11977:9', '1:19364:5'),
        InterRulesIssue('1:11977:9', '1:19365:5'), InterRulesIssue('1:11977:9', '1:20301:4'),
        InterRulesIssue('1:11979:7', '1:20382:4'), InterRulesIssue('1:11980:9', '1:20387:5'),
        InterRulesIssue('1:11980:9', '1:20388:5'), InterRulesIssue('1:11980:9', '1:20389:4'),
        InterRulesIssue('1:11983:7', '1:20383:4'), InterRulesIssue('1:11984:7', '1:20384:4'),
        InterRulesIssue('1:12001:7', '1:20385:4'), InterRulesIssue('1:12005:7', '1:20386:4'),
        InterRulesIssue('1:12682:8', '1:51761:4'), InterRulesIssue('1:12682:8', '1:51767:4'),
        InterRulesIssue('1:12682:8', '1:51772:2'), InterRulesIssue('1:13693:12', '1:19364:5'),
        InterRulesIssue('1:13693:12', '1:19365:5'), InterRulesIssue('1:13693:12', '1:20390:9'),
        InterRulesIssue('1:16351:11', '1:51508:4'), InterRulesIssue('1:16351:11', '1:51509:4'),
        InterRulesIssue('1:16351:11', '1:51744:2'), InterRulesIssue('1:16351:11', '1:51760:4'),
        InterRulesIssue('1:16351:11', '1:51761:4'), InterRulesIssue('1:16351:11', '1:51772:2'),
        InterRulesIssue('1:16351:11', '1:52093:1'), InterRulesIssue('1:19334:5', '1:51760:4'),
        InterRulesIssue('1:19334:5', '1:51761:4'), InterRulesIssue('1:19334:5', '1:51767:4'),
        InterRulesIssue('1:19334:5', '1:51772:2'), InterRulesIssue('1:19336:6', '1:51760:4'),
        InterRulesIssue('1:19336:6', '1:51761:4'), InterRulesIssue('1:19336:6', '1:51767:4'),
        InterRulesIssue('1:19336:6', '1:51772:2'), InterRulesIssue('1:19364:5', '1:19365:5'),
        InterRulesIssue('1:19364:5', '1:20300:4'), InterRulesIssue('1:19364:5', '1:20301:4'),
        InterRulesIssue('1:19364:5', '1:20308:4'), InterRulesIssue('1:19364:5', '1:20387:5'),
        InterRulesIssue('1:19364:5', '1:20388:5'), InterRulesIssue('1:19364:5', '1:20390:9'),
        InterRulesIssue('1:19364:5', '1:21150:6'), InterRulesIssue('1:19364:5', '1:51492:2'),
        InterRulesIssue('1:19364:5', '1:51494:3'), InterRulesIssue('1:19364:5', '1:51495:2'),
        InterRulesIssue('1:19364:5', '1:51499:2'), InterRulesIssue('1:19364:5', '1:51506:2'),
        InterRulesIssue('1:19364:5', '1:51512:2'), InterRulesIssue('1:19364:5', '1:51513:2'),
        InterRulesIssue('1:19364:5', '1:51515:2'), InterRulesIssue('1:19364:5', '1:51747:2'),
        InterRulesIssue('1:19364:5', '1:51749:3'), InterRulesIssue('1:19364:5', '1:51751:2'),
        InterRulesIssue('1:19364:5', '1:51754:2'), InterRulesIssue('1:19364:5', '1:51758:2'),
        InterRulesIssue('1:19364:5', '1:51769:2'), InterRulesIssue('1:19364:5', '1:51770:2'),
        InterRulesIssue('1:19364:5', '1:51771:2'), InterRulesIssue('1:19364:5', '1:52087:2'),
        InterRulesIssue('1:19364:5', '1:52088:1'), InterRulesIssue('1:19364:5', '1:52090:1'),
        InterRulesIssue('1:19364:5', '1:52091:2'), InterRulesIssue('1:19364:5', '1:52092:1'),
        InterRulesIssue('1:19364:5', '1:52093:1'), InterRulesIssue('1:19364:5', '1:52326:1'),
        InterRulesIssue('1:19364:5', '1:52327:1'), InterRulesIssue('1:19364:5', '1:57683:1'),
        InterRulesIssue('1:19364:5', '1:57684:1'), InterRulesIssue('1:19364:5', '1:60447:1'),
        InterRulesIssue('1:19364:5', '1:60448:1'), InterRulesIssue('1:19365:5', '1:20300:4'),
        InterRulesIssue('1:19365:5', '1:20301:4'), InterRulesIssue('1:19365:5', '1:20308:4'),
        InterRulesIssue('1:19365:5', '1:20387:5'), InterRulesIssue('1:19365:5', '1:20388:5'),
        InterRulesIssue('1:19365:5', '1:20390:9'), InterRulesIssue('1:19365:5', '1:21150:6'),
        InterRulesIssue('1:19365:5', '1:51492:2'), InterRulesIssue('1:19365:5', '1:51494:3'),
        InterRulesIssue('1:19365:5', '1:51495:2'), InterRulesIssue('1:19365:5', '1:51499:2'),
        InterRulesIssue('1:19365:5', '1:51506:2'), InterRulesIssue('1:19365:5', '1:51512:2'),
        InterRulesIssue('1:19365:5', '1:51513:2'), InterRulesIssue('1:19365:5', '1:51515:2'),
        InterRulesIssue('1:19365:5', '1:51745:2'), InterRulesIssue('1:19365:5', '1:51747:2'),
        InterRulesIssue('1:19365:5', '1:51749:3'), InterRulesIssue('1:19365:5', '1:51751:2'),
        InterRulesIssue('1:19365:5', '1:51754:2'), InterRulesIssue('1:19365:5', '1:51758:2'),
        InterRulesIssue('1:19365:5', '1:51769:2'), InterRulesIssue('1:19365:5', '1:51770:2'),
        InterRulesIssue('1:19365:5', '1:51771:2'), InterRulesIssue('1:19365:5', '1:51773:2'),
        InterRulesIssue('1:19365:5', '1:52087:2'), InterRulesIssue('1:19365:5', '1:52088:1'),
        InterRulesIssue('1:19365:5', '1:52090:1'), InterRulesIssue('1:19365:5', '1:52091:2'),
        InterRulesIssue('1:19365:5', '1:52092:1'), InterRulesIssue('1:19365:5', '1:52093:1'),
        InterRulesIssue('1:19365:5', '1:52326:1'), InterRulesIssue('1:19365:5', '1:52327:1'),
        InterRulesIssue('1:19365:5', '1:57683:1'), InterRulesIssue('1:19365:5', '1:57684:1'),
        InterRulesIssue('1:19365:5', '1:60447:1'), InterRulesIssue('1:19365:5', '1:60448:1'),
        InterRulesIssue('1:19373:5', '1:19374:5'), InterRulesIssue('1:19375:5', '1:19376:5'),
        InterRulesIssue('1:19377:5', '1:19378:5'), InterRulesIssue('1:19379:5', '1:19380:5'),
        InterRulesIssue('1:19381:5', '1:19382:5'), InterRulesIssue('1:19383:5', '1:19384:5'),
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
        InterRulesIssue('1:20387:5', '1:20389:4'), InterRulesIssue('1:20388:5', '1:20389:4'),
        InterRulesIssue('1:20424:4', '1:51760:4'), InterRulesIssue('1:20424:4', '1:51767:4'),
        InterRulesIssue('1:20424:4', '1:51772:2'), InterRulesIssue('1:51492:2', '1:51747:2'),
        InterRulesIssue('1:51493:2', '1:51750:2'), InterRulesIssue('1:51494:3', '1:51745:2'),
        InterRulesIssue('1:51494:3', '1:51749:3'), InterRulesIssue('1:51494:3', '1:51773:2'),
        InterRulesIssue('1:51495:2', '1:51751:2'), InterRulesIssue('1:51497:2', '1:51753:2'),
        InterRulesIssue('1:51499:2', '1:51754:2'), InterRulesIssue('1:51504:4', '1:51767:4'),
        InterRulesIssue('1:51506:2', '1:51758:2'), InterRulesIssue('1:51508:4', '1:51509:4'),
        InterRulesIssue('1:51508:4', '1:51760:4'), InterRulesIssue('1:51508:4', '1:51761:4'),
        InterRulesIssue('1:51508:4', '1:52093:1'), InterRulesIssue('1:51509:4', '1:51760:4'),
        InterRulesIssue('1:51509:4', '1:51761:4'), InterRulesIssue('1:51509:4', '1:52093:1'),
        InterRulesIssue('1:51512:2', '1:51771:2'), InterRulesIssue('1:51513:2', '1:51769:2'),
        InterRulesIssue('1:51515:2', '1:51770:2'), InterRulesIssue('1:51744:2', '1:51772:2'),
        InterRulesIssue('1:51744:2', '1:52093:1'), InterRulesIssue('1:51745:2', '1:51749:3'),
        InterRulesIssue('1:51745:2', '1:51773:2'), InterRulesIssue('1:51749:3', '1:51773:2'),
        InterRulesIssue('1:51760:4', '1:51761:4'), InterRulesIssue('1:51760:4', '1:52093:1'),
        InterRulesIssue('1:51761:4', '1:52093:1'), InterRulesIssue('1:51772:2', '1:52093:1'),
        InterRulesIssue('1:52087:2', '1:52091:2'), InterRulesIssue('1:52088:1', '1:52092:1'),
        InterRulesIssue('1:52090:1', '1:52093:1'), InterRulesIssue('1:52326:1', '1:52327:1'),
        InterRulesIssue('1:57683:1', '1:57684:1'), InterRulesIssue('1:60447:1', '1:60448:1'),
    }


    ############################################################################################
    ############################################################################################


    http_crude_rules = {
        # http_chrome
        # http_firefox
        "1:29579:3", "1:29625:3", "1:44978:3",
        # http_webkit
        # http_other
        # http_ie
        "1:33492:3", "1:42040:5", "1:45154:2",
        # http_plugins
        "1:12448:19", "1:13523:31", "1:13699:12", "1:13758:10", "1:15670:18", "1:15678:10", "1:18325:9", "1:18592:11",
        "1:20708:12", "1:21063:13", "1:21076:11", "1:23291:7", "1:25565:5", "1:25566:5", "1:26975:3", "1:27173:5",
        "1:37995:1", "1:38383:2", "1:39168:2", "1:39372:2", "1:4167:16", "1:41827:1", "1:41829:1", "1:46404:2", "1:51413:1",
        "1:8375:12",
    }

    http_chameleon_rules = {
        # http_chrome
        "1:35411:3",
        # http_firefox
        "1:40363:2",
        # http_webkit
        "1:19010:10", "1:19095:10", "1:51391:1",
        # http_other
        "1:15462:23", "1:16481:14", "1:38382:2", "1:56845:2", "1:56846:2",
        # http_ie
        "1:12277:19", "1:15732:12", "1:17303:12", "1:17311:6", "1:17768:15", "1:19149:13", "1:19150:13", "1:19171:12",
        "1:19245:12", "1:19872:7", "1:23125:11", "1:26137:3", "1:26220:3", "1:26636:6", "1:26883:5", "1:27150:7",
        "1:27716:2", "1:30127:2", "1:30849:4", "1:34772:3", "1:35975:2", "1:35999:3", "1:36605:2", "1:36791:2", "1:3683:13",
        "1:37614:2", "1:38085:3", "1:39505:3", "1:40146:4", "1:40659:2", "1:40669:3", "1:41719:2", "1:41720:2", "1:41772:2",
        "1:43460:2", "1:43461:2", "1:43465:2", "1:44510:2", "1:44548:2", "1:44823:2", "1:46929:1", "1:47474:1", "1:47732:1",
        "1:47738:1", "1:49365:1", "1:51419:1", "1:54232:1", "1:56286:1", "1:63980:1", "1:63982:1", "1:6509:16", "1:6510:15",
        # http_plugins
        "1:10084:12", "1:10128:15", "1:10162:12", "1:10189:14", "1:10192:25", "1:10387:14", "1:10390:14", "1:10393:15",
        "1:10404:13", "1:10419:12", "1:10423:11", "1:11176:19", "1:11181:17", "1:11187:17", "1:11199:18", "1:11259:14",
        "1:11673:8", "1:11822:14", "1:12010:11", "1:12087:9", "1:12193:15", "1:12203:14", "1:12382:9", "1:12384:8",
        "1:12407:12", "1:12434:9", "1:12448:19", "1:12452:14", "1:12459:17", "1:12466:12", "1:12472:19", "1:12612:12",
        "1:12729:12", "1:13219:17", "1:13224:15", "1:13232:10", "1:13258:15", "1:13262:15", "1:13294:14", "1:13296:14",
        "1:13303:14", "1:13419:21", "1:13426:12", "1:13430:12", "1:13547:10", "1:13679:13", "1:13685:10", "1:13699:12",
        "1:14266:12", "1:14594:11", "1:14596:12", "1:14603:12", "1:14611:14", "1:14637:11", "1:14746:12", "1:14748:13",
        "1:14752:13", "1:14756:14", "1:14764:15", "1:14778:12", "1:14993:10", "1:14997:10", "1:14999:10", "1:15003:11",
        "1:15084:10", "1:15088:11", "1:15092:11", "1:15096:10", "1:15109:12", "1:15122:15", "1:15159:9", "1:15177:9",
        "1:15181:10", "1:15228:9", "1:15230:14", "1:15232:10", "1:15247:9", "1:15249:9", "1:15251:9", "1:15270:9",
        "1:15274:9", "1:15278:9", "1:15282:9", "1:15284:9", "1:15288:9", "1:15330:9", "1:15332:9", "1:15334:10",
        "1:15338:10", "1:15342:10", "1:15346:9", "1:15350:9", "1:15368:9", "1:15372:9", "1:15376:10", "1:15557:9",
        "1:15679:12", "1:15858:12", "1:15861:16", "1:15878:9", "1:16379:9", "1:16386:7", "1:16569:9", "1:16746:10",
        "1:16767:9", "1:16772:13", "1:16779:8", "1:16783:9", "1:16791:7", "1:16802:7", "1:17061:7", "1:17063:8",
        "1:17065:8", "1:17067:8", "1:17069:8", "1:17071:8", "1:17073:8", "1:17078:7", "1:17082:7", "1:17084:7", "1:17092:9",
        "1:17096:8", "1:17099:8", "1:17171:8", "1:17464:9", "1:17614:9", "1:17670:9", "1:17674:9", "1:18321:11",
        "1:18323:9", "1:18325:9", "1:18668:15", "1:18741:7", "1:18904:11", "1:19102:12", "1:19108:13", "1:19193:12",
        "1:19197:12", "1:19304:10", "1:19561:9", "1:19562:10", "1:19564:10", "1:19650:10", "1:20175:12", "1:20536:9",
        "1:20537:7", "1:20573:6", "1:20875:7", "1:20949:7", "1:21022:7", "1:21029:7", "1:21031:7", "1:21033:7", "1:21493:7",
        "1:21589:5", "1:23186:10", "1:23352:10", "1:24281:8", "1:24559:7", "1:24578:3", "1:25299:7", "1:25344:8",
        "1:26497:4", "1:26764:5", "1:26766:5", "1:27174:5", "1:27175:5", "1:27179:4", "1:27282:5", "1:27742:4", "1:27743:4",
        "1:28126:5", "1:28762:6", "1:30092:2", "1:31043:2", "1:31335:3", "1:32632:3", "1:34638:2", "1:34918:3", "1:35622:2",
        "1:4213:15", "1:43185:2", "1:43309:2", "1:43606:3", "1:49638:1", "1:7866:18", "1:8403:10", "1:8738:19", "1:9629:16",
        "1:9793:17", "1:9795:15", "1:9798:15",
    }

    http_stutter_rules = set()

    http_duplicate_rules = {
        # http_chrome
        # http_firefox
        # http_webkit
        # http_other
        # http_ie
        InterRulesIssue('1:23609:9', '1:31469:2'), InterRulesIssue('1:27829:2', '1:27830:2'),
        InterRulesIssue('1:33492:3', '1:45154:2'), InterRulesIssue('1:35998:3', '1:35999:3'),
        InterRulesIssue('1:41625:4', '1:41763:3'),
        # http_plugins
        InterRulesIssue('1:10193:21', '1:10194:22'), InterRulesIssue('1:10414:10', '1:10417:10'),
        InterRulesIssue('1:11189:14', '1:11201:13'),
        InterRulesIssue('1:13436:13', '1:13444:13'), InterRulesIssue('1:13758:10', '1:4167:16'),
        InterRulesIssue('1:20708:12', '1:21063:13', '1:21076:11'),
    }

    http_overlapping_rules = {
        # http_chrome
        # http_firefox
        InterRulesIssue('1:17213:9', '1:17629:13'), InterRulesIssue('1:25289:3', '1:25290:3'),
        InterRulesIssue('1:29579:3', '1:44978:3'),
        # http_webkit
        # http_other
        # http_ie
        InterRulesIssue('1:19873:14', '1:25329:8'), InterRulesIssue('1:20809:11', '1:20810:11'),
        InterRulesIssue('1:26132:5', '1:44736:1'), InterRulesIssue('1:26569:4', '1:26668:3'),
        InterRulesIssue('1:26634:5', '1:27061:3'), InterRulesIssue('1:31204:3', '1:31403:5'),
        InterRulesIssue('1:33492:3', '1:33493:2'), InterRulesIssue('1:33493:2', '1:45154:2'),
        InterRulesIssue('1:34727:4', '1:36559:5'), InterRulesIssue('1:36431:4', '1:42032:2'),
        InterRulesIssue('1:40364:6', '1:41797:2'), InterRulesIssue('1:41718:2', '1:41719:2'),
        InterRulesIssue('1:41718:2', '1:41720:2'), InterRulesIssue('1:42040:5', '1:43110:2'),
        InterRulesIssue('1:42040:5', '1:46763:1'), InterRulesIssue('1:42040:5', '1:47082:2'),
        InterRulesIssue('1:44153:2', '1:44192:2'), InterRulesIssue('1:48772:1', '1:48781:1'),
        InterRulesIssue('1:53918:1', '1:54193:1'), InterRulesIssue('1:53924:1', '1:54193:1'),
        # http_plugins
        InterRulesIssue('1:10189:14', '1:43371:2'), InterRulesIssue('1:10191:9', '1:43373:2'),
        InterRulesIssue('1:10192:25', '1:17425:13'), InterRulesIssue('1:11178:15', '1:11189:14'),
        InterRulesIssue('1:11178:15', '1:11201:13'), InterRulesIssue('1:11224:12', '1:37507:3'),
        InterRulesIssue('1:11293:11', '1:36865:2'), InterRulesIssue('1:12083:10', '1:43342:2'),
        InterRulesIssue('1:12203:14', '1:14278:12'), InterRulesIssue('1:12205:10', '1:14280:11'),
        InterRulesIssue('1:12248:10', '1:12252:10'),
        InterRulesIssue('1:12382:9', '1:52469:1'), InterRulesIssue('1:12448:19', '1:8852:15'),
        InterRulesIssue('1:12450:15', '1:8854:14'), InterRulesIssue('1:13232:10', '1:16581:10'),
        InterRulesIssue('1:13262:15', '1:51413:1'), InterRulesIssue('1:13446:11', '1:13785:10'),
        InterRulesIssue('1:13523:31', '1:19925:8'), InterRulesIssue('1:13523:31', '1:24676:9'),
        InterRulesIssue('1:13539:15', '1:16672:11'), InterRulesIssue('1:13699:12', '1:14025:14'),
        InterRulesIssue('1:13699:12', '1:14029:11'),
        InterRulesIssue('1:14326:12', '1:4233:15'), InterRulesIssue('1:14756:14', '1:32754:2'),
        InterRulesIssue('1:15232:10', '1:37005:2'), InterRulesIssue('1:15280:9', '1:30048:4'),
        InterRulesIssue('1:15632:13', '1:16602:10'), InterRulesIssue('1:15670:18', '1:15678:10'),
        InterRulesIssue('1:15687:11', '1:15855:10'),
        InterRulesIssue('1:16068:11', '1:18592:11'), InterRulesIssue('1:16510:15', '1:19893:10'),
        InterRulesIssue('1:16573:9', '1:17571:9'), InterRulesIssue('1:16607:11', '1:46404:2'),
        InterRulesIssue('1:16671:15', '1:51413:1'), InterRulesIssue('1:16740:6', '1:20901:6'),
        InterRulesIssue('1:17160:14', '1:17163:10'), InterRulesIssue('1:18325:9', '1:21022:7'),
        InterRulesIssue('1:18325:9', '1:26378:4'), InterRulesIssue('1:19650:10', '1:27173:5'),
        InterRulesIssue('1:19909:10', '1:27173:5'), InterRulesIssue('1:20175:12', '1:37995:1'),
        InterRulesIssue('1:20573:6', '1:39372:2'), InterRulesIssue('1:21022:7', '1:26378:4'),
        InterRulesIssue('1:21029:7', '1:39381:2'), InterRulesIssue('1:21030:7', '1:39383:2'),
        InterRulesIssue('1:21918:13', '1:39167:2'), InterRulesIssue('1:21918:13', '1:39168:2'),
        InterRulesIssue('1:21919:13', '1:39168:2'), InterRulesIssue('1:23290:7', '1:23291:7'),
        InterRulesIssue('1:23291:7', '1:23296:7'), InterRulesIssue('1:23291:7', '1:23299:7'),
        InterRulesIssue('1:23395:13', '1:35327:3'), InterRulesIssue('1:23396:9', '1:35329:3'),
        InterRulesIssue('1:23985:10', '1:8375:12'), InterRulesIssue('1:24559:7', '1:29059:7'),
        InterRulesIssue('1:24560:7', '1:29060:7'), InterRulesIssue('1:25111:6', '1:25113:6'),
        InterRulesIssue('1:25565:5', '1:39372:2'), InterRulesIssue('1:26363:11', '1:37995:1'),
        InterRulesIssue('1:26364:11', '1:37996:1'), InterRulesIssue('1:27206:5', '1:27207:4'),
        InterRulesIssue('1:28750:6', '1:28759:6'), InterRulesIssue('1:28751:6', '1:28760:6'),
        InterRulesIssue('1:28755:6', '1:28761:6'), InterRulesIssue('1:28756:6', '1:28757:6'),
        InterRulesIssue('1:28765:6', '1:28766:6'), InterRulesIssue('1:28768:6', '1:28769:6'),
        InterRulesIssue('1:28772:6', '1:28787:6'), InterRulesIssue('1:28775:6', '1:28788:6'),
        InterRulesIssue('1:28776:6', '1:28777:6'), InterRulesIssue('1:28780:6', '1:28781:6'),
        InterRulesIssue('1:28784:6', '1:28789:6'), InterRulesIssue('1:34455:3', '1:41829:1'),
        InterRulesIssue('1:34639:2', '1:34640:2'), InterRulesIssue('1:34919:3', '1:34922:3'),
        InterRulesIssue('1:36640:3', '1:38383:2'), InterRulesIssue('1:36662:2', '1:38383:2'),
        InterRulesIssue('1:37512:2', '1:38435:2'), InterRulesIssue('1:38230:3', '1:41827:1'),
        InterRulesIssue('1:38231:3', '1:41829:1'), InterRulesIssue('1:39038:2', '1:41803:2'),
        InterRulesIssue('1:39970:2', '1:45286:2'), InterRulesIssue('1:41491:2', '1:41500:3'),
        InterRulesIssue('1:43185:2', '1:48541:1'),
    }

    http_orthogonal_rules = {
        # http_chrome
        # http_firefox
        InterRulesIssue('1:18186:6', '1:43642:4'), InterRulesIssue('1:19076:9', '1:19292:7'),
        InterRulesIssue('1:19713:9', '1:29625:3'), InterRulesIssue('1:19714:6', '1:29625:3'),
        # http_webkit
        # http_other
        # http_ie
        InterRulesIssue('1:11257:11', '1:16007:11'), InterRulesIssue('1:13453:12', '1:40669:3'),
        InterRulesIssue('1:17726:14', '1:32709:2'),
        InterRulesIssue('1:17769:13', '1:19436:14'), InterRulesIssue('1:18196:18', '1:18240:15'),
        InterRulesIssue('1:18221:15', '1:19873:14'),
        InterRulesIssue('1:23609:9', '1:31469:2'), InterRulesIssue('1:26848:7', '1:29716:3'),
        InterRulesIssue('1:27829:2', '1:27830:2'), InterRulesIssue('1:27830:2', '1:35133:3'),
        InterRulesIssue('1:32471:4', '1:32629:3'), InterRulesIssue('1:33492:3', '1:45154:2'),
        InterRulesIssue('1:35998:3', '1:35999:3'), InterRulesIssue('1:35999:3', '1:49128:1'),
        InterRulesIssue('1:39220:3', '1:49725:2'), InterRulesIssue('1:40715:3', '1:42040:5'),
        InterRulesIssue('1:40715:3', '1:46763:1'), InterRulesIssue('1:40973:2', '1:41561:3'),
        InterRulesIssue('1:41625:4', '1:41763:3'), InterRulesIssue('1:49118:1', '1:49725:2'),
        InterRulesIssue('1:51419:1', '1:51420:2'),
        # http_plugins
        InterRulesIssue('1:10193:21', '1:10194:22'), InterRulesIssue('1:10414:10', '1:10417:10'),
        InterRulesIssue('1:11189:14', '1:11201:13'),
        InterRulesIssue('1:11230:11', '1:37040:2'), InterRulesIssue('1:11234:11', '1:37043:2'),
        InterRulesIssue('1:12384:8', '1:26355:11'), InterRulesIssue('1:12442:9', '1:43649:2'),
        InterRulesIssue('1:12472:19', '1:29578:4'), InterRulesIssue('1:12600:9', '1:43375:2'),
        InterRulesIssue('1:12604:9', '1:43377:2'), InterRulesIssue('1:13260:14', '1:51406:1'),
        InterRulesIssue('1:13264:14', '1:51407:1'), InterRulesIssue('1:13426:12', '1:18592:11'),
        InterRulesIssue('1:13434:14', '1:26974:3'),
        InterRulesIssue('1:13436:13', '1:13444:13'), InterRulesIssue('1:13436:13', '1:26975:3'),
        InterRulesIssue('1:13440:13', '1:26975:3'), InterRulesIssue('1:13444:13', '1:26975:3'),
        InterRulesIssue('1:13523:31', '1:17557:13'), InterRulesIssue('1:13525:27', '1:24675:8'),
        InterRulesIssue('1:13758:10', '1:4167:16'), InterRulesIssue('1:13913:17', '1:16388:7'),
        InterRulesIssue('1:14765:10', '1:8740:13'), InterRulesIssue('1:15245:9', '1:17226:8'),
        InterRulesIssue('1:15268:9', '1:37022:1'), InterRulesIssue('1:15274:9', '1:36653:3'),
        InterRulesIssue('1:15278:9', '1:30050:4'), InterRulesIssue('1:15670:18', '1:15679:12'),
        InterRulesIssue('1:15678:10', '1:15679:12'), InterRulesIssue('1:16386:7', '1:9626:18'),
        InterRulesIssue('1:17545:9', '1:24773:9'), InterRulesIssue('1:19151:14', '1:19152:13'),
        InterRulesIssue('1:19197:12', '1:48901:2'), InterRulesIssue('1:20573:6', '1:25565:5'),
        InterRulesIssue('1:20574:6', '1:25566:5'), InterRulesIssue('1:20708:12', '1:21063:13'),
        InterRulesIssue('1:20708:12', '1:21076:11'),
        InterRulesIssue('1:21063:13', '1:21076:11'), InterRulesIssue('1:23352:10', '1:25254:5'),
        InterRulesIssue('1:23372:7', '1:36487:3'), InterRulesIssue('1:23374:7', '1:36490:3'),
        InterRulesIssue('1:23376:7', '1:36485:3'), InterRulesIssue('1:24772:6', '1:51408:1'),
        InterRulesIssue('1:24773:9', '1:51410:1'), InterRulesIssue('1:25111:6', '1:25565:5'),
        InterRulesIssue('1:25112:7', '1:25566:5'), InterRulesIssue('1:25113:6', '1:25565:5'),
        InterRulesIssue('1:31043:2', '1:8375:12'), InterRulesIssue('1:34454:3', '1:41827:1'),
        InterRulesIssue('1:39167:2', '1:39168:2'), InterRulesIssue('1:39971:2', '1:45288:2'),
        InterRulesIssue('1:46404:2', '1:8383:15'),
    }


    ############################################################################################
    ############################################################################################






passthrough_issues = PassThroughIssues()