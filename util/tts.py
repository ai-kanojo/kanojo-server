from infer.modules.vc.modules import VC
from configs.config import Config
from pydub import AudioSegment
from google.cloud import texttospeech

class CharacterTTS:
    """
    텍스트를 케릭터의 목소리로 음성변환해줍니다.
    """

    def __init__(self, model_name : str) -> None:
        self.config = Config()
        self.vc = VC(self.config)
        self.vc.get_vc(model_name,0.33,0.33)
        self.client = texttospeech.TextToSpeechClient()

    def text_to_speech_kr(self, txt : str, audio_path : str) -> AudioSegment:
        """
        텍스트를 입력받아 케릭터 음성으로 변환해 반환
        """
        # 기본 세팅
        index_path = "assets\\weights\\added_IVF460_Flat_nprobe_1_Szrv3_v2.index"

        #google tts
        synthesis_input = texttospeech.SynthesisInput(text=txt)
        voice = texttospeech.VoiceSelectionParams(
            language_code="ko-KR", name="ko-KR-Neural2-A", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

                # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(audio_path, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)

        #RVC를 이용한 변환
        opt1,opt2 = self.vc.vc_single(
            sid=0,
            input_audio_path=audio_path,
            f0_up_key=0,
            f0_file="",
            f0_method="rmvpe",
            file_index=index_path,
            file_index2="",
            index_rate=0,
            filter_radius=3.0,
            resample_sr=0,
            rms_mix_rate=0.25,
            protect=0.33
        )

        audio_segment = AudioSegment(
            opt2[1],
            frame_rate=opt2[0],
            sample_width=opt2[1].dtype.itemsize,
            channels=1
        )

        audio_segment.export(audio_path, format="wav")

    def text_to_speech_jp(self, txt : str, audio_path : str) -> AudioSegment:
        """
        텍스트를 입력받아 케릭터 음성으로 변환해 반환
        """
        # 기본 세팅
        index_path = "assets\\weights\\added_IVF460_Flat_nprobe_1_Szrv3_v2.index"

        #google tts
        synthesis_input = texttospeech.SynthesisInput(text=txt)
        voice = texttospeech.VoiceSelectionParams(
            language_code="jp-JP", name="jp-JP-Neural2-B", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

                # voice parameters and audio file type
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(audio_path, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)

        #RVC를 이용한 변환
        opt1,opt2 = self.vc.vc_single(
            sid=0,
            input_audio_path=audio_path,
            f0_up_key=0,
            f0_file="",
            f0_method="rmvpe",
            file_index=index_path,
            file_index2="",
            index_rate=0,
            filter_radius=3.0,
            resample_sr=0,
            rms_mix_rate=0.25,
            protect=0.33
        )

        audio_segment = AudioSegment(
            opt2[1],
            frame_rate=opt2[0],
            sample_width=opt2[1].dtype.itemsize,
            channels=1
        )

        audio_segment.export(audio_path, format="wav")
