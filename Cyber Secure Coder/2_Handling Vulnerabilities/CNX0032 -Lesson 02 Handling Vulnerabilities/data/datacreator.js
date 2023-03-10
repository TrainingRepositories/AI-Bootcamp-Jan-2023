/* jslint node: true */
'use strict'

var models = require('../models/index')
var datacache = require('./datacache')
var config = require('config')
var utils = require('../lib/utils')
var challenges = datacache.challenges
var users = datacache.users
var products = datacache.products

module.exports = function () {
  createChallenges()
  createUsers()
  createRandomFakeUsers()
  createProducts()
  createBaskets()
  createFeedback()

  function createChallenges () {
    const addHint = function (hint) {
      return config.get('application.showChallengeHints') ? hint : null
    }

    models.Challenge.create({
      name: 'Score Board',
      category: 'Information Leakage',
      description: 'Find the carefully hidden \'Score Board\' page.',
      difficulty: 1,
      hint: addHint('Try to find a reference or clue behind the scenes. Or simply guess what URL the Score Board might have.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/score-board.html#find-the-carefully-hidden-score-board-page'),
      solved: false
    }).success(function (challenge) {
      challenges.scoreBoardChallenge = challenge
    })
    models.Challenge.create({
      name: 'Error Handling',
      category: 'Information Leakage',
      description: 'Provoke an error that is not very gracefully handled.',
      difficulty: 1,
      hint: addHint('Try to submit bad input to forms. Alternatively tamper with URL paths or parameters.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/leakage.html#provoke-an-error-that-is-not-very-gracefully-handled'),
      solved: false
    }).success(function (challenge) {
      challenges.errorHandlingChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login Admin',
      category: 'SQL Injection',
      description: 'Log in with the administrator\'s user account.',
      difficulty: 2,
      hint: addHint('Try different SQL Injection attack patterns depending whether you know the admin\'s email address or not.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/sqli.html#log-in-with-the-administrators-user-account'),
      solved: false
    }).success(function (challenge) {
      challenges.loginAdminChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login Jim',
      category: 'SQL Injection',
      description: 'Log in with Jim\'s user account.',
      difficulty: 3,
      hint: addHint('Try cracking Jim\'s password hash if you harvested it already. Alternatively, if you know Jim\'s email address, try SQL Injection.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/sqli.html#log-in-with-jims-user-account'),
      solved: false
    }).success(function (challenge) {
      challenges.loginJimChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login Bender',
      category: 'SQL Injection',
      description: 'Log in with Bender\'s user account.',
      difficulty: 3,
      hint: addHint('If you know Bender\'s email address, try SQL Injection. Bender\'s password hash might not help you very much.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/sqli.html#log-in-with-benders-user-account'),
      solved: false
    }).success(function (challenge) {
      challenges.loginBenderChallenge = challenge
    })
    models.Challenge.create({
      name: 'XSS Tier 1',
      category: 'XSS',
      description: 'XSS Tier 1: Perform a <i>reflected</i> XSS attack with <code>&lt;script&gt;alert("XSS1")&lt;/script&gt;</code>.',
      difficulty: 1,
      hint: addHint('Look for an input field where its content appears in the response HTML when its form is submitted.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/xss.html#xss-tier-1-perform-a-reflected-xss-attack'),
      solved: false
    }).success(function (challenge) {
      challenges.localXssChallenge = challenge
    })
    models.Challenge.create({
      name: 'XSS Tier 2',
      category: 'XSS',
      description: 'XSS Tier 2: Perform a <i>persisted</i> XSS attack with <code>&lt;script&gt;alert("XSS2")&lt;/script&gt;</code> bypassing a <i>client-side</i> security mechanism.',
      difficulty: 3,
      hint: addHint('Only some input fields validate their input. Even less of these are persisted in a way where their content is shown on another screen.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/xss.html#xss-tier-2-perform-a-persisted-xss-attack-bypassing-a-client-side-security-mechanism'),
      solved: false
    }).success(function (challenge) {
      challenges.persistedXssChallengeUser = challenge
    })
    models.Challenge.create({
      name: 'XSS Tier 4',
      category: 'XSS',
      description: 'XSS Tier 4: Perform a <i>persisted</i> XSS attack with <code>&lt;script&gt;alert("XSS4")&lt;/script&gt;</code> bypassing a <i>server-side</i> security mechanism.',
      difficulty: 4,
      hint: addHint('The "Comment" field in the "Contact Us" screen is where you want to put your focus on.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/xss.html#xss-tier-4-perform-a-persisted-xss-attack-bypassing-a-server-side-security-mechanism'),
      solved: false
    }).success(function (challenge) {
      challenges.persistedXssChallengeFeedback = challenge
    })
    models.Challenge.create({
      name: 'XSS Tier 3',
      category: 'XSS',
      description: 'XSS Tier 3: Perform a <i>persisted</i> XSS attack with <code>&lt;script&gt;alert("XSS3")&lt;/script&gt;</code> without using the frontend application at all.',
      difficulty: 3,
      hint: addHint('You need to work with the server-side API directly. Try different HTTP verbs on different entities exposed through the API.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/xss.html#xss-tier-3-perform-a-persisted-xss-attack-without-using-the-frontend-application-at-all'),
      solved: false
    }).success(function (challenge) {
      challenges.restfulXssChallenge = challenge
    })
    models.Challenge.create({
      name: 'User Credentials',
      category: 'SQL Injection',
      description: 'Retrieve a list of all user credentials via SQL Injection',
      difficulty: 3,
      hint: addHint('Craft a UNION SELECT attack string against a page where you can influence the data being displayed.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/sqli.html#retrieve-a-list-of-all-user-credentials-via-sql-injection'),
      solved: false
    }).success(function (challenge) {
      challenges.unionSqlInjectionChallenge = challenge
    })
    models.Challenge.create({
      name: 'Password Strength',
      category: 'Weak Security Mechanisms',
      description: 'Log in with the administrator\'s user credentials without previously changing them or applying SQL Injection.',
      difficulty: 2,
      hint: addHint('This one should be equally easy to a) brute force, b) crack the password hash or c) simply guess.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/weak-security.html#log-in-with-the-administrators-user-credentials-without-previously-changing-them-or-applying-sql-injection'),
      solved: false
    }).success(function (challenge) {
      challenges.weakPasswordChallenge = challenge
    })
    models.Challenge.create({
      name: 'Five-Star Feedback',
      category: 'Privilege Escalation',
      description: 'Get rid of all 5-star customer feedback.',
      difficulty: 1,
      hint: addHint('Once you found admin section of the application, this challenge is almost trivial.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/privilege-escalation.html#get-rid-of-all-5-star-customer-feedback'),
      solved: false
    }).success(function (challenge) {
      challenges.feedbackChallenge = challenge
    })
    models.Challenge.create({
      name: 'Forged Feedback',
      category: 'Privilege Escalation',
      description: 'Post some feedback in another users name.',
      difficulty: 3,
      hint: addHint('You can solve this by tampering with the user interface or by intercepting the communication with the RESTful backend.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/privilege-escalation.html#post-some-feedback-in-another-users-name'),
      solved: false
    }).success(function (challenge) {
      challenges.forgedFeedbackChallenge = challenge
    })
    models.Challenge.create({
      name: 'Redirects',
      category: 'Weak Security Mechanisms',
      description: 'Wherever you go, there you are.',
      difficulty: 4,
      hint: addHint('You have to find a way to beat the whitelist of allowed redirect URLs.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/weak-security.html#wherever-you-go-there-you-are'),
      solved: false
    }).success(function (challenge) {
      challenges.redirectChallenge = challenge
    })
    models.Challenge.create({
      name: 'Basket Access',
      category: 'Privilege Escalation',
      description: 'Access someone else\'s basket.',
      difficulty: 2,
      hint: addHint('Have an eye on the HTTP traffic while shopping. Alternatively try to find s client-side association of users to their basket.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/privilege-escalation.html#access-someone-elses-basket'),
      solved: false
    }).success(function (challenge) {
      challenges.basketChallenge = challenge
    })
    models.Challenge.create({
      name: 'Payback Time',
      category: 'Validation Flaws',
      description: 'Place an order that makes you rich.',
      difficulty: 3,
      hint: addHint('You literally need to make the shop owe you any amount of money.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/validation.html#place-an-order-that-makes-you-rich'),
      solved: false
    }).success(function (challenge) {
      challenges.negativeOrderChallenge = challenge
    })
    models.Challenge.create({
      name: 'Confidential Document',
      category: 'Forgotten Content',
      description: 'Access a confidential document.',
      difficulty: 1,
      hint: addHint('Analyze and tamper with links in the application that deliver a file directly.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#access-a-confidential-document'),
      solved: false
    }).success(function (challenge) {
      challenges.directoryListingChallenge = challenge
    })
    models.Challenge.create({
      name: 'Forgotten Developer Backup',
      category: 'Forgotten Content',
      description: 'Access a developer\'s forgotten backup file.',
      difficulty: 3,
      hint: addHint('You need to trick a security mechanism into thinking that the file you want has a valid file type.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#access-a-developers-forgotten-backup-file'),
      solved: false
    }).success(function (challenge) {
      challenges.forgottenDevBackupChallenge = challenge
    })
    models.Challenge.create({
      name: 'Forgotten Sales Backup',
      category: 'Forgotten Content',
      description: 'Access a salesman\'s forgotten backup file.',
      difficulty: 2,
      hint: addHint('You need to trick a security mechanism into thinking that the file you want has a valid file type.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#access-a-salesmans-forgotten-backup-file'),
      solved: false
    }).success(function (challenge) {
      challenges.forgottenBackupChallenge = challenge
    })
    models.Challenge.create({
      name: 'Admin Section',
      category: 'Privilege Escalation',
      description: 'Access the administration section of the store.',
      difficulty: 1,
      hint: addHint('It is just slightly harder to find than the score board link.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/privilege-escalation.html#access-the-administration-section-of-the-store'),
      solved: false
    }).success(function (challenge) {
      challenges.adminSectionChallenge = challenge
    })
    models.Challenge.create({
      name: 'CSRF',
      category: 'CSRF',
      description: 'Change Bender\'s password into <i>slurmCl4ssic</i> without using SQL Injection.',
      difficulty: 4,
      hint: addHint('The fact that this challenge is in the CSRF category is already a huge hint.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/csrf.html#change-benders-password-into-slurmcl4ssic-without-using-sql-injection'),
      solved: false
    }).success(function (challenge) {
      challenges.csrfChallenge = challenge
    })
    models.Challenge.create({
      name: 'Product Tampering',
      category: 'Privilege Escalation',
      description: 'Change the <code>href</code> of the link within the <a href="/#/search?q=O-Saft">O-Saft product</a> description into <i>http://kimminich.de</i>.',
      difficulty: 3,
      hint: addHint('Look for one of the following: a) broken admin functionality, b) holes in RESTful API or c) possibility for SQL Injection.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/privilege-escalation.html#change-the-href-of-the-link-within-the-o-saft-product-description'),
      solved: false
    }).success(function (challenge) {
      challenges.changeProductChallenge = challenge
    })
    models.Challenge.create({
      name: 'Vulnerable Component',
      category: 'Cryptographic Issues',
      description: '<a href="/#/contact">Inform the shop</a> about a vulnerable library it is using. (Mention the exact library name and version in your comment.)',
      difficulty: 3,
      hint: addHint('Report one of two possible answers via the "Contact Us" form. Do not forget to submit the library\'s version as well.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#inform-the-shop-about-a-vulnerable-library-it-is-using'),
      solved: false
    }).success(function (challenge) {
      challenges.knownVulnerableComponentChallenge = challenge
    })
    models.Challenge.create({
      name: 'Weird Crypto',
      category: 'Cryptographic Issues',
      description: '<a href="/#/contact">Inform the shop</a> about an algorithm or library it should definitely not use the way it does.',
      difficulty: 2,
      hint: addHint('Report one of four possible answers via the "Contact Us" form.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#inform-the-shop-about-an-algorithm-or-library-it-should-definitely-not-use-the-way-it-does'),
      solved: false
    }).success(function (challenge) {
      challenges.weirdCryptoChallenge = challenge
    })
    models.Challenge.create({
      name: 'Easter Egg Tier 1',
      category: 'Forgotten Content',
      description: 'Find the hidden <a href="http://en.wikipedia.org/wiki/Easter_egg_(media)" target="_blank">easter egg</a>.',
      difficulty: 3,
      hint: addHint('If you solved one of the three file access challenges, you already know where to find the easter egg.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#find-the-hidden-easter-egg'),
      solved: false
    }).success(function (challenge) {
      challenges.easterEggLevelOneChallenge = challenge
    })
    models.Challenge.create({
      name: 'Easter Egg Tier 2',
      category: 'Cryptographic Issues',
      description: 'Apply some advanced cryptanalysis to find <i>the real</i> easter egg.',
      difficulty: 4,
      hint: addHint('You might have to peel through several layers of tough-as-nails encryption for this challenge.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#apply-some-advanced-cryptanalysis-to-find-the-real-easter-egg'),
      solved: false
    }).success(function (challenge) {
      challenges.easterEggLevelTwoChallenge = challenge
    })
    models.Challenge.create({
      name: 'Forged Coupon',
      category: 'Cryptographic Issues',
      description: 'Forge a coupon code that gives you a discount of at least 80%.',
      difficulty: 5,
      hint: addHint('Try either a) a knowledgable brute force attack or b) reverse engineering.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#forge-a-coupon-code-that-gives-you-a-discount-of-at-least-80'),
      solved: false
    }).success(function (challenge) {
      challenges.forgedCouponChallenge = challenge
    })
    models.Challenge.create({
      name: 'Eye Candy',
      category: 'Forgotten Content',
      description: 'Travel back in time to the golden era of <img src="/css/geo-bootstrap/img/hot.gif"> web design.',
      difficulty: 3,
      hint: addHint('The mentioned golden era lasted from 1994 to 2009.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#travel-back-in-time-to-the-golden-era-of-web-design'),
      solved: false
    }).success(function (challenge) {
      challenges.geocitiesThemeChallenge = challenge
    })
    models.Challenge.create({
      name: 'Christmas Special',
      category: 'SQL Injection',
      description: 'Order the Christmas special offer of 2014.',
      difficulty: 2,
      hint: addHint('Find out how the application handles unavailable products.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/sqli.html#order-the-christmas-special-offer-of-2014'),
      solved: false
    }).success(function (challenge) {
      challenges.christmasSpecialChallenge = challenge
    })
    models.Challenge.create({
      name: 'Upload Size',
      category: 'Validation Flaws',
      description: 'Upload a file larger than 100 kB.',
      difficulty: 3,
      hint: addHint('You can attach a small file to the "File Complaint" form. Investigate how this upload actually works.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/validation.html#upload-a-file-larger-than-100-kb'),
      solved: false
    }).success(function (challenge) {
      challenges.uploadSizeChallenge = challenge
    })
    models.Challenge.create({
      name: 'Upload Type',
      category: 'Validation Flaws',
      description: 'Upload a file that has no .pdf extension.',
      difficulty: 3,
      hint: addHint('You can attach a PDF file to the "File Complaint" form. Investigate how this upload actually works.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/validation.html#upload-a-file-that-has-no-pdf-extension'),
      solved: false
    }).success(function (challenge) {
      challenges.uploadTypeChallenge = challenge
    })
    models.Challenge.create({
      name: 'Extra Language',
      category: 'Forgotten Content',
      description: 'Retrieve the language file that never made it into production.',
      difficulty: 4,
      hint: addHint('Brute force is not the only option for this challenge, but a perfectly viable one.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/forgotten-content.html#retrieve-the-language-file-that-never-made-it-into-production'),
      solved: false
    }).success(function (challenge) {
      challenges.extraLanguageChallenge = challenge
    })
    models.Challenge.create({
      name: 'Zero Stars',
      category: 'Validation Flaws',
      description: 'Give a devastating zero-star feedback to the store.',
      difficulty: 1,
      hint: addHint('Before you invest time bypassing the API, you might want to play around with the UI a bit.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/validation.html#give-a-devastating-zero-star-feedback-to-the-store'),
      solved: false
    }).success(function (challenge) {
      challenges.zeroStarsChallenge = challenge
    })
    models.Challenge.create({
      name: 'Imaginary Challenge',
      category: 'Cryptographic Issues',
      description: 'Solve challenge #99. Unfortunately, this challenge does not exist.',
      difficulty: 5,
      hint: addHint('You need to trick the hacking progress persistence feature into thinking you solved challenge #99.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#solve-challenge-99'),
      solved: false
    }).success(function (challenge) {
      challenges.continueCodeChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login Bjoern',
      category: 'Weak Security Mechanisms',
      description: 'Log in with Bjoern\'s user account <i>without</i> previously changing his password, applying SQL Injection, or hacking his Google account.',
      difficulty: 3,
      hint: addHint('The security flaw behind this challenge is 100% Juice Shop\'s fault and 0% Google\'s.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/weak-security.html#log-in-with-bjoerns-user-account'),
      solved: false
    }).success(function (challenge) {
      challenges.oauthUserPasswordChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login CISO',
      category: 'Weak Security Mechanisms',
      description: 'Exploit OAuth 2.0 to log in with the Chief Information Security Officer\'s user account.',
      difficulty: 4,
      hint: addHint('Don\'t try to beat Google\'s OAuth 2.0 service. Rather investigate implementation flaws on Juice Shop\'s end.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/weak-security.html#exploit-oauth-20-to-log-in-with-the-cisos-user-account'),
      solved: false
    }).success(function (challenge) {
      challenges.loginCisoChallenge = challenge
    })
    models.Challenge.create({
      name: 'Login Support Team',
      category: 'Weak Security Mechanisms',
      description: 'Log in with the support team\'s original user credentials without applying SQL Injection or any other bypass.',
      difficulty: 5,
      hint: addHint('The underlying flaw of this challenge is a lot more human error than technical weakness.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/weak-security.html#log-in-with-the-support-teams-original-user-credentials'),
      solved: false
    }).success(function (challenge) {
      challenges.loginSupportChallenge = challenge
    })
    models.Challenge.create({
      name: 'Premium Paywall',
      category: 'Cryptographic Issues',
      description: '<i class="fa fa-diamond"></i><i class="fa fa-diamond"></i><i class="fa fa-diamond"></i><i class="fa fa-diamond"></i><i class="fa fa-diamond"></i><!--R9U8AvGlBbjhHXHW422jxVL2hoLBr8wflIAQ8d/jlERpKnrNlMErs1JfgT9EK/kzTtdb1GPhuWAz3i2HhomhaFMxvg4na+tvTi+8DoQoeqZH1KADoM2NJ7UOKc14b54cdRTXiYV7yFUzbPjjPVOWZFSmDcG6z+jQIPZtJuJ/tQc=--> <a href="/redirect?to=https://blockchain.info/address/1AbKfgvw9psQ41NbLi8kufDQTezwG8DRZm" target="_blank" class="btn btn-danger btn-xs"><i class="fa fa-btc fa-sm"></i> Unlock Premium Challenge</a> to access exclusive content.',
      difficulty: 5,
      hint: addHint('You do not have to pay anything to unlock this challenge! Nonetheless, donations are very much appreciated.'),
      hintUrl: addHint('https://bkimminich.gitbooks.io/pwning-owasp-juice-shop/content/part2/crypto.html#unlock-premium-challenge-to-access-exclusive-content'),
      solved: false
    }).success(function (challenge) {
      challenges.premiumPaywallChallenge = challenge
    })
  }

  function createUsers () {
    models.User.create({
      email: 'admin@' + config.get('application.domain'),
      password: 'admin123'
    })
    models.User.create({
      email: 'jim@' + config.get('application.domain'),
      password: 'ncc-1701'
    })
    models.User.create({
      email: 'bender@' + config.get('application.domain'),
      password: 'OhG0dPlease1nsertLiquor!'
    }).success(function (user) {
      users.bender = user
    })
    models.User.create({
      email: 'bjoern.kimminich@googlemail.com',
      password: 'YmpvZXJuLmtpbW1pbmljaEBnb29nbGVtYWlsLmNvbQ=='
    }).success(function (user) {
      users.bjoern = user
    })
    models.User.create({
      email: 'ciso@' + config.get('application.domain'),
      password: 'mDLx?94T~1CfVfZMzw@sJ9f?s3L6lbMqE70FfI8^54jbNikY5fymx7c!YbJb'
    }).success(function (user) {
      users.ciso = user
    })
    models.User.create({
      email: 'support@' + config.get('application.domain'),
      password: 'J6aVjTgOpRs$?5l+Zkq2AYnCE@RF??P'
    }).success(function (user) {
      users.support = user
    })
  }

  function createRandomFakeUsers () {
    for (var i = 0; i < config.get('application.numberOfRandomFakeUsers'); i++) {
      models.User.create({
        email: getGeneratedRandomFakeUserEmail(),
        password: makeRandomString(5)
      })
    }
  }

  function getGeneratedRandomFakeUserEmail () {
    var randomDomain = makeRandomString(4).toLowerCase() + '.' + makeRandomString(2).toLowerCase()
    return makeRandomString(5).toLowerCase() + '@' + randomDomain
  }

  function makeRandomString (length) {
    var text = ''
    var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for (var i = 0; i < length; i++) { text += possible.charAt(Math.floor(Math.random() * possible.length)) }

    return text
  }

  function createProducts () {
    for (var i = 0; i < config.get('products').length; i++) {
      var product = config.get('products')[i]
      var name = product.name
      var description = product.description || 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.'
      if (product.useForChristmasSpecialChallenge) {
        description += ' (Seasonal special offer! Limited availability!)'
      } else if (product.useForProductTamperingChallenge) {
        description += ' <a href="https://www.owasp.org/index.php/O-Saft" target="_blank">More...</a>'
      }
      var price = product.price || Math.floor(Math.random())
      var image = product.image || 'undefined.png'
      if (utils.startsWith(image, 'http')) {
        var imageUrl = image
        image = decodeURIComponent(image.substring(image.lastIndexOf('/') + 1))
        utils.downloadToFile(imageUrl, 'app/public/images/products/' + image)
      }
      models.Product.create({
        name: name,
        description: description,
        price: price,
        image: image
      }).success(function (product) {
        if (product.description.match(/Seasonal special offer! Limited availability!/)) {
          products.christmasSpecial = product
          models.sequelize.query('UPDATE Products SET deletedAt = \'2014-12-27 00:00:00.000 +00:00\' WHERE id = ' + product.id)
        } else if (product.description.match(/a href="https:\/\/www\.owasp\.org\/index\.php\/O-Saft"/)) {
          products.osaft = product
        }
      })
    }
  }

  function createBaskets () {
    models.Basket.create({
      UserId: 1
    })
    models.Basket.create({
      UserId: 2
    })
    models.Basket.create({
      UserId: 3
    })
    models.BasketItem.create({
      BasketId: 1,
      ProductId: 1,
      quantity: 2
    })
    models.BasketItem.create({
      BasketId: 1,
      ProductId: 2,
      quantity: 3
    })
    models.BasketItem.create({
      BasketId: 1,
      ProductId: 3,
      quantity: 1
    })
    models.BasketItem.create({
      BasketId: 2,
      ProductId: 4,
      quantity: 2
    })
    models.BasketItem.create({
      BasketId: 3,
      ProductId: 5,
      quantity: 1
    })
  }

  function createFeedback () {
    models.Feedback.create({
      UserId: 1,
      comment: 'I love this shop! Best products in town! Highly recommended!',
      rating: 5
    })
    models.Feedback.create({
      UserId: 2,
      comment: 'Great shop! Awesome service!',
      rating: 4
    })
    models.Feedback.create({
      comment: 'Incompetent customer support! Can\'t even upload photo of broken purchase!<br><em>Support Team: Sorry, only order confirmation PDFs can be attached to complaints!</em>',
      rating: 2
    })
    models.Feedback.create({
      comment: 'This is <b>the</b> store for awesome stuff of all kinds!',
      rating: 4
    })
    models.Feedback.create({
      comment: 'Never gonna buy anywhere else from now on! Thanks for the great service!',
      rating: 4
    })
    models.Feedback.create({
      comment: 'Keep up the good work!',
      rating: 3
    })
    models.Feedback.create({
      UserId: 3,
      comment: 'Nothing useful available here!',
      rating: 1
    })
  }
}
