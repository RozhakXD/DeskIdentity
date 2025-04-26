import random
from abc import ABC, abstractmethod
from typing import Dict, List


class BrowserVersionGenerator:
    @staticmethod
    def generate_chrome_version() -> str:
        chrome_major_version = random.randint(100, 135)
        chrome_build_version = random.randint(0, 9999)
        chrome_patch_version = random.randint(0, 9999)
        return f"{chrome_major_version}.0.{chrome_build_version}.{chrome_patch_version}"

    @staticmethod
    def generate_firefox_version() -> str:
        firefox_major_version = random.randint(80, 127)
        return f"{firefox_major_version}.0"

    @staticmethod
    def generate_opera_version() -> str:
        opera_major_version = random.randint(80, 117)
        opera_build_version = random.randint(0, 9999)
        opera_patch_version = random.randint(0, 9999)
        return f"{opera_major_version}.0.{opera_build_version}.{opera_patch_version}"

    @staticmethod
    def generate_edge_version() -> str:
        edge_major_version = random.randint(80, 135)
        edge_build_version = random.randint(0, 9999)
        edge_patch_version = random.randint(0, 9999)
        return f"{edge_major_version}.0.{edge_build_version}.{edge_patch_version}"

    @staticmethod
    def generate_brave_version() -> str:
        brave_patch = random.randint(100, 120)
        brave_minor = random.randint(30, 40)
        return f"1.{brave_minor}.{brave_patch}"

    @staticmethod
    def generate_yandex_version() -> str:
        yandex_minor = random.randint(1, 15)
        yandex_patch = random.randint(1, 5)
        yandex_build = random.randint(500, 800)
        return f"22.{yandex_minor}.{yandex_patch}.{yandex_build}"

    @staticmethod
    def generate_uc_version() -> str:
        uc_major = random.randint(13, 15)
        uc_minor = random.randint(0, 9)
        uc_patch = random.randint(0, 10)
        uc_build = random.randint(1000, 1500)
        return f"{uc_major}.{uc_minor}.{uc_patch}.{uc_build}"

    @staticmethod
    def generate_safari_version() -> str:
        safari_major = random.randint(10, 17)
        safari_minor = random.randint(0, 9)
        return f"{safari_major}.{safari_minor}"


class UserAgentGenerator(ABC):
    def __init__(self):
        self.browser_versions = BrowserVersionGenerator()

    @abstractmethod
    def generate(self, browser: str) -> str:
        pass


class WindowsUserAgentGenerator(UserAgentGenerator):
    def generate(self, browser: str) -> str:
        windows_version = random.choice([
            "Windows NT 10.0", "Windows NT 6.3", "Windows NT 6.2",
            "Windows NT 6.1", "Windows NT 6.0", "Windows NT 5.2",
            "Windows NT 5.1", "Windows NT 5.01", "Windows NT 5.0",
        ])

        operating_system = random.choice([
            "WOW64; rv:84.0", "ARM; Touch", "Win64", "Win64; x64",
            "Win64; ARM", "Win64; IA-64", "Win32", "Win32; x64",
            "Win32; ARM", "Win32; IA-64",
        ])

        if browser == "chrome":
            chrome_version = self.browser_versions.generate_chrome_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
        elif browser == "firefox":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}'
        elif browser == "opera":
            chrome_version = self.browser_versions.generate_chrome_version()
            opera_version = self.browser_versions.generate_opera_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{opera_version}'
        elif browser == "edge":
            chrome_version = self.browser_versions.generate_chrome_version()
            edge_version = self.browser_versions.generate_edge_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edg/{edge_version}'
        elif browser == "tor":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}'
        elif browser == "yandex":
            chrome_version = self.browser_versions.generate_chrome_version()
            yandex_version = self.browser_versions.generate_yandex_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Yandex/{yandex_version}'
        else:  # UC
            chrome_version = self.browser_versions.generate_chrome_version()
            uc_version = self.browser_versions.generate_uc_version()
            return f'Mozilla/5.0 ({windows_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 UBrowser/{uc_version}'


class LinuxUserAgentGenerator(UserAgentGenerator):
    def generate(self, browser: str) -> str:
        linux_version = random.choice([
            "X11; Arch Linux", "X11; Ubuntu", "X11; Debian",
            "X11; Fedora", "X11; Linux Mint",
        ])

        operating_system = random.choice([
            "Linux aarch64", "Linux x86_64", "Linux sparc64",
            "Linux i686", "Linux mips64", "Linux i586",
            "Linux armv7l", "Linux arm64", "Linux ppc64le",
            "Linux s390x", "Linux riscv64",
        ])

        if browser == "chrome":
            chrome_version = self.browser_versions.generate_chrome_version()
            return f'Mozilla/5.0 ({linux_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
        elif browser == "firefox":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 ({linux_version}; {operating_system}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}'
        elif browser == "opera":
            chrome_version = self.browser_versions.generate_chrome_version()
            opera_version = self.browser_versions.generate_opera_version()
            return f'Mozilla/5.0 ({linux_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{opera_version}'
        elif browser == "edge":
            chrome_version = self.browser_versions.generate_chrome_version()
            edge_version = self.browser_versions.generate_edge_version()
            return f'Mozilla/5.0 ({linux_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edg/{edge_version}'
        else:  # Brave
            chrome_version = self.browser_versions.generate_chrome_version()
            brave_version = self.browser_versions.generate_brave_version()
            return f'Mozilla/5.0 ({linux_version}; {operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Brave/{brave_version}'


class MacOSUserAgentGenerator(UserAgentGenerator):
    def generate(self, browser: str) -> str:
        mac_version = random.choice([
            "10_14_6", "10_12_6", "11_0_1", "10_11_6", "10_10_5",
            "10_9_5", "10_8_5", "10_4_11", "10_2_8", "10_0_4",
            "10_1_5", "10_3_9", "10_7_5", "10_15_7", "10_6_8",
            "10_5_8", "10_13_6",
        ])

        if browser == "chrome":
            chrome_version = self.browser_versions.generate_chrome_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
        elif browser == "firefox":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}'
        elif browser == "edge":
            chrome_version = self.browser_versions.generate_chrome_version()
            edge_version = self.browser_versions.generate_edge_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edge/{edge_version}'
        elif browser == "opera":
            chrome_version = self.browser_versions.generate_chrome_version()
            opera_version = self.browser_versions.generate_opera_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{opera_version}'
        elif browser == "brave":
            chrome_version = self.browser_versions.generate_chrome_version()
            brave_version = self.browser_versions.generate_brave_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Brave/{brave_version}'
        else:  # Safari
            safari_version = self.browser_versions.generate_safari_version()
            return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/537.36 (KHTML, like Gecko) Version/{safari_version} Safari/537.36'


class FreeBSDUserAgentGenerator(UserAgentGenerator):
    def generate(self, browser: str) -> str:
        operating_system = random.choice([
            "FreeBSD; powerpc64", "FreeBSD; amd64", "FreeBSD; i386",
            "FreeBSD; sparc64", "FreeBSD; arm64", "FreeBSD; riscv64",
        ])

        if browser == "chrome":
            chrome_version = self.browser_versions.generate_chrome_version()
            return f'Mozilla/5.0 ({operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
        elif browser == "firefox":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 ({operating_system}) Gecko/20100101 Firefox/{firefox_version}'
        elif browser == "opera":
            chrome_version = self.browser_versions.generate_chrome_version()
            opera_version = self.browser_versions.generate_opera_version()
            return f'Mozilla/5.0 ({operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 OPR/{opera_version}'
        else:  # Edge
            chrome_version = self.browser_versions.generate_chrome_version()
            edge_version = self.browser_versions.generate_edge_version()
            return f'Mozilla/5.0 ({operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36 Edg/{edge_version}'


class HaikuOSUserAgentGenerator(UserAgentGenerator):
    def generate(self, browser: str) -> str:
        operating_system = random.choice([
            "BeOS; U; BeOS R5 Final Edition", "BeOS; U; BeOS 5.0 Final",
            "BeOS; U; BeOS R5", "BeOS; U; BeOS R5.1",
            "BeOS; U; BeOS R5 Test Build", "BeOS; U; BeOS 4.5",
            "BeOS; U; BeOS R5", "BeOS; U; BeOS 4.2",
            "BeOS; R5", "BeOS; U; BeOS R5 Pro",
            "BeOS; U; BeOS R5.1", "BeOS; U; BeOS R4",
            "BeOS; U; BeOS Alpha Build", "Haiku; U; Haiku",
            "Haiku; U; Haiku 1.0",
        ])

        locale = random.choice([
            "en-AU", "en-US", "en-CA", "fr-CA", "de-AT",
            "pt-PT", "nl-NL", "pl-PL", "zh-CN", "ko-KR",
            "ru-RU", "ja-JP", "it-IT", "pt-BR", "es-ES",
            "de-DE", "en-GB"
        ])

        if browser == "chrome":
            chrome_version = self.browser_versions.generate_chrome_version()
            return f'Mozilla/5.0 ({operating_system}; {locale}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36'
        elif browser == "firefox":
            firefox_version = self.browser_versions.generate_firefox_version()
            return f'Mozilla/5.0 ({operating_system}; {locale}) Gecko/20100101 Firefox/{firefox_version}'
        else:  # Edge
            edge_version = self.browser_versions.generate_edge_version()
            return f'Mozilla/5.0 ({operating_system}; {locale}) AppleWebKit/537.36 (KHTML, like Gecko) Edge/{edge_version}'


class UserAgentFactory:
    @staticmethod
    def get_generator(os_type: str) -> UserAgentGenerator:
        generators = {
            "windows": WindowsUserAgentGenerator,
            "linux": LinuxUserAgentGenerator,
            "macos": MacOSUserAgentGenerator,
            "freebsd": FreeBSDUserAgentGenerator,
            "haikuos": HaikuOSUserAgentGenerator,
        }

        generator_class = generators.get(os_type.lower())
        if not generator_class:
            raise ValueError(f"Unsupported OS type: {os_type}")

        return generator_class()


class UserAgentService:
    def __init__(self):
        self.factory = UserAgentFactory()

    def generate_user_agents(self, os_type: str, browser: str, count: int = 1, unique: bool = True) -> List[str]:
        generator = self.factory.get_generator(os_type)
        user_agents = set() if unique else []

        for _ in range(count):
            ua = generator.generate(browser)
            if unique:
                user_agents.add(ua)
            else:
                user_agents.append(ua)

        return list(user_agents) if unique else user_agents